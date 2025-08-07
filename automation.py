from dotenv import load_dotenv
load_dotenv()
import os
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import time
import logging
from datetime import datetime
from tqdm.asyncio import tqdm
import os

class MusicDeliveryAutomation:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path
        self.login_url = os.getenv("MUSICDELIVERY_LOGIN_URL")
        self.email = os.getenv("MUSICDELIVERY_EMAIL")
        self.password = os.getenv("MUSICDELIVERY_PASSWORD")

        
        # Configuração do sistema de logging
        self.setup_logging()
        
        # Contadores para estatísticas
        self.processed_links = 0
        self.successful_links = 0
        self.failed_links = 0
        
    def setup_logging(self):
        """Configura o sistema de logging"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f'logs/musicdelivery_{timestamp}.log'
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("=" * 50)
        self.logger.info("INICIANDO AUTOMAÇÃO MUSICDELIVERY")
        self.logger.info("=" * 50)
        
    async def run_automation(self):
        start_time = datetime.now()
        self.logger.info(f"Iniciando automação às {start_time.strftime('%H:%M:%S')}")
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                await self.login(page)
                links = self.read_excel_links()
                
                if not links:
                    self.logger.error("Nenhum link encontrado para processar")
                    return
                
                await self.process_links(page, links)
                
                end_time = datetime.now()
                duration = end_time - start_time
                self.generate_final_report(duration)
                
            except Exception as e:
                self.logger.error(f"Erro crítico durante a automação: {str(e)}")
            finally:
                await browser.close()
                self.logger.info("Navegador fechado - Automação finalizada")
    
    async def login(self, page):
        self.logger.info("Iniciando processo de login...")
        
        try:
            await page.goto(self.login_url)
            self.logger.info(f"Navegando para: {self.login_url}")
            await page.wait_for_load_state('networkidle')
            
            await page.fill('//*[@id="login-username"]', self.email)
            self.logger.info(f"Email preenchido: {self.email}")
            
            await page.fill('//*[@id="login-password"]', self.password)
            self.logger.info("Senha preenchida")
            
            await page.locator('//html/body/div[1]/div/div/div/div[2]/form/div[4]/div/button').click() 
            self.logger.info("Botão de login clicado")
            
            await page.wait_for_load_state('networkidle')
            self.logger.info("✅ Login realizado com sucesso!")
            
        except Exception as e:
            self.logger.error(f"❌ Erro durante o login: {str(e)}")
            raise
    
    def read_excel_links(self):
        try:
            self.logger.info(f"Lendo arquivo Excel: {self.excel_file_path}")
            df = pd.read_excel(self.excel_file_path)
            
            if 'links' in df.columns:
                links = df['links'].dropna().tolist()
            else:
                links = df.iloc[:, 0].dropna().tolist()
                self.logger.warning("Coluna 'links' não encontrada. Usando primeira coluna.")
            
            self.logger.info(f"✅ {len(links)} links encontrados para processar")
            
            if links:
                self.logger.info("Primeiros links encontrados:")
                for i, link in enumerate(links[:5], 1):
                    self.logger.info(f"  {i}. {link}")
                if len(links) > 5:
                    self.logger.info(f"  ... e mais {len(links) - 5} links")
            
            return links
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao ler arquivo Excel: {str(e)}")
            return []
    
    async def process_links(self, page, links):
        total_links = len(links)
        self.logger.info(f"Iniciando processamento de {total_links} links")
        
        progress_bar = tqdm(
            total=total_links,
            desc="Processando links",
            unit="link",
            colour="green",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {rate_fmt}"
        )
        
        for index, link in enumerate(links, 1):
            try:
                progress_bar.set_description(f"Link {index}/{total_links}")
                self.logger.info(f"Processando link {index}/{total_links}: {link}")
                
                await page.goto(link)
                await page.wait_for_load_state('networkidle')
                await asyncio.sleep(1)

                # Rola a página para baix
                await page.keyboard.press("End")
                self.logger.info("🔽 Scroll até o final da página com tecla 'End'")
                await asyncio.sleep(1)
                
                try:
                    await page.wait_for_selector('//*[@id="btn-confirmar-recebimento"]', timeout=10000)

                    # Intercepta o prompt e envia string vazia (ou "ok" se preferir)
                    page.once("dialog", lambda dialog: asyncio.create_task(dialog.accept("")))
                    
                    await page.click('//*[@id="btn-confirmar-recebimento"]')
                    self.logger.info(f"✅ Botão 'confirmar recebimento' clicado e prompt aceito - Link {index}")
                    
                    self.successful_links += 1
                    await asyncio.sleep(3)
                    
                except Exception as button_error:
                    self.logger.error(f"❌ Erro ao processar botão no link {index}: {str(button_error)}")
                    self.failed_links += 1
                    continue
                    
            except Exception as link_error:
                self.logger.error(f"❌ Erro ao processar link {index}: {str(link_error)}")
                self.failed_links += 1
                continue
            finally:
                self.processed_links += 1
                progress_bar.update(1)
        
        progress_bar.close()
        self.logger.info("✅ Processamento de todos os links concluído!")
    
    def generate_final_report(self, duration):
        self.logger.info("=" * 50)
        self.logger.info("RELATÓRIO FINAL DA AUTOMAÇÃO")
        self.logger.info("=" * 50)
        self.logger.info(f"Total de links processados: {self.processed_links}")
        self.logger.info(f"Links processados com sucesso: {self.successful_links}")
        self.logger.info(f"Links com falha: {self.failed_links}")
        
        if self.processed_links > 0:
            success_rate = (self.successful_links / self.processed_links) * 100
            self.logger.info(f"Taxa de sucesso: {success_rate:.2f}%")
        
        self.logger.info(f"Tempo total de execução: {duration}")
        self.logger.info("=" * 50)

async def main():
    excel_file = "arquivo.xlsx"
    automation = MusicDeliveryAutomation(excel_file)
    await automation.run_automation()

if __name__ == "__main__":
    asyncio.run(main())
