import os
from dotenv import load_dotenv

load_dotenv()

# ========== CONFIGURAÇÕES DE LOGIN ==========
LOGIN_URL = os.getenv("MUSICDELIVERY_LOGIN_URL")
EMAIL = os.getenv("MUSICDELIVERY_EMAIL")
PASSWORD = os.getenv("MUSICDELIVERY_PASSWORD")

# ========== CAMINHOS DE ARQUIVOS =========
EXCEL_FILE = "arquivo.xlsx"  # Caminho para o arquivo Excel com os links
LOG_DIRECTORY = "logs"       # Diretório para salvar os logs

# ========== SELETORES XPATH ==========
SELECTORS = {
    "login_username": '//*[@id="login-username"]',
    "login_password": '//*[@id="login-password"]',
    "login_button": '/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/button',
    "confirm_button": '//*[@id="btn-confirmar-recebimento"]'
}

# ========== TIMEOUTS (em milissegundos) ==========
TIMEOUTS = {
    "page_load": 30000,        # Timeout para carregamento da página
    "button_wait": 10000,      # Timeout para aguardar botão aparecer
    "popup_wait": 5000         # Timeout para aguardar popu
}

# ========== DELAYS (em segundos) ==========
DELAYS = {
    "after_login": 3,          # Delay após login
    "page_load": 2,            # Delay após carregar página
    "after_click": 2,          # Delay após clicar no botão
    "between_links": 3,        # Delay entre processamento de links
    "popup_response": 1        # Delay antes de confirmar popup
}

# ========== CONFIGURAÇÕES DO NAVEGADOR ==========
BROWSER_CONFIG = {
    "headless": False,         # True para executar sem interface gráfica
    "slow_mo": 500,           # Delay entre ações do navegador (ms)
    "timeout": 30000          # Timeout geral do navegador
}

# ========== CONFIGURAÇÕES DE LOG ==========
LOG_CONFIG = {
    "level": "INFO",          # Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "max_file_size": 10,      # MB - Tamanho máximo do arquivo de log
    "backup_count": 5         # Número de backups de log para manter
}

# ========== CONFIGURAÇÕES DO EXCEL ==========
EXCEL_CONFIG = {
    "link_column": "links",   # Nome da coluna que contém os links
    "sheet_name": 0,          # Nome ou índice da planilha (0 = primeira)
    "skip_rows": 0            # Número de linhas para pular no início
}

# ========== CONFIGURAÇÕES DE PROGRESSO ==========
PROGRESS_CONFIG = {
    "show_progress": True,    # Mostrar barra de progresso
    "progress_color": "green", # Cor da barra de progresso
    "show_rate": True,        # Mostrar taxa de processamento
    "show_eta": True          # Mostrar tempo estimado
}

# ========== CONFIGURAÇÕES DE RELATÓRIO ==========
REPORT_CONFIG = {
    "save_detailed_report": True,     # Salvar relatório detalhado
    "report_directory": "reports",    # Diretório para salvar relatórios
    "include_timestamps": True,       # Incluir timestamps no relatório
    "include_error_details": True     # Incluir detalhes dos erros
}

# ========== CONFIGURAÇÕES DE RECOVERY ==========
RECOVERY_CONFIG = {
    "retry_failed_links": False,      # Tentar reprocessar links com falha
    "max_retries": 3,                 # Número máximo de tentativas
    "retry_delay": 5,                 # Delay entre tentativas (segundos)
    "save_failed_links": True         # Salvar links com falha para reprocessamento
}