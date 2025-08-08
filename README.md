# 🎼 Automation

Automação em Python com Playwright para acessar o sistema [MusicDelivery], realizar login e confirmar o recebimento de parcelas a partir de uma lista de links fornecida via planilha Excel.

---

## 📌 Funcionalidades

- ✅ Login automatizado no sistema MusicDelivery
- 📊 Leitura de links a partir de um arquivo Excel
- 🖱️ Scroll automático na página
- 🎯 Clique no botão "Confirmar Recebimento"
- 💬 Resposta automática ao `prompt()` do sistema
- 📝 Logs detalhados de execução
- 📊 Barra de progresso com TQDM
- 📋 Relatório final de sucesso/falha

---

## 📂 Estrutura do Projeto

```bash
musicdelivery-automation/
│
├── config_example.py         # Modelo de configuração sem dados sensíveis
├── script.py                 # Script principal da automação
├── arquivo.xlsx              # Planilha com os links a serem processados
├── .env                      # (IGNORADO) Armazena credenciais reais
├── .gitignore                # Ignora arquivos sensíveis e temporários
├── logs/                     # Logs de execução
├── screenshots/              # Capturas de tela em caso de erro
└── README.md                 # Este arquivo
```

---

## ⚙️ Requisitos

- Python 3.8+
- Playwright
- pandas
- tqdm
- python-dotenv

---

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/musicdelivery-automation.git
cd musicdelivery-automation
```

### 2. Crie e ative um ambiente virtual (opcional mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Instale o Playwright
```bash
playwright install
```

---

---

## 📊 Preparação do Arquivo Excel

1. Abra o arquivo `arquivo.xlsx`
2. Na **coluna A** (primeira coluna), insira os links que deseja processar
3. **Não adicione cabeçalho** - comece diretamente com os links na primeira linha
4. Salve o arquivo

**Exemplo:**
```
A1: http://sistema.com.br/parcela/123

```

---

## 🧪 Execução

1. Certifique-se de que o arquivo `.env` está configurado
2. Verifique se o arquivo `arquivo.xlsx` contém os links
3. Execute a automação:

```bash
python script.py
```



## 📈 Funcionamento

O script realizará as seguintes ações para cada link:

1. 🔐 **Login Automático**: Acessa o sistema com as credenciais do `.env`
2. 🌐 **Navegação**: Acessa cada URL da planilha
3. 📜 **Scroll**: Rola a página para localizar elementos
4. 🎯 **Clique**: Encontra e clica no botão "Confirmar Recebimento"
5. 💬 **Prompt**: Responde automaticamente ao prompt de confirmação
6. 📝 **Log**: Registra sucesso ou falha da operação

---

## ✅ Resultado

Ao final da execução, você verá:

- 📊 **Relatório no Terminal**: Quantidade de sucessos e falhas
- 📝 **Logs Detalhados**: Arquivo salvo em `logs/automation_YYYY-MM-DD_HH-MM-SS.log`
- 🖼️ **Screenshots**: Capturas de tela salvas em caso de erro (pasta `screenshots/`)

**Exemplo de saída:**
```
🎵 Automation - Relatório Final
============================================
✅ Processados com sucesso: 15
❌ Falharam: 2
📊 Total processados: 17
⏱️ Tempo total: 3m 45s
```

---

## 🛡️ Segurança

- 🔒 **Dados Sensíveis**: Protegidos via arquivo `.env`
- 🚫 **Versionamento**: `config.py` e `.env` não são versionados
- 📸 **Debug**: Capturas de tela automáticas em caso de erro
- 📝 **Logs**: Registros detalhados para auditoria

---

## 🐛 Solução de Problemas

### Erro de Login
- Verifique as credenciais no arquivo `.env`
- Confirme se a URL de login está correta

### Erro ao Processar Links
- Verifique se o arquivo `arquivo.xlsx` existe
- Confirme se os links estão na coluna A
- Verifique se os links são válidos

### Playwright não Funciona
```bash
# Reinstalar Playwright
pip uninstall playwright
pip install playwright
playwright install
```

### Elementos não Encontrados
- Verifique os screenshots na pasta `screenshots/`
- Analise os logs em `logs/` para mais detalhes

---

## 📋 requirements.txt

```txt
playwright==1.40.0
pandas==2.1.4
tqdm==4.66.1
python-dotenv==1.0.0
openpyxl==3.1.2
```

---

## 📝 Licença

Este projeto é **privado** e voltado para uso interno. Para obter permissão de uso ou cópia, entre em contato com o mantenedor.

---

## 👨‍💻 Autor

**Desenvolvido por**: Suporte Técnico  


--

## 🔄 Versões

- **v1.0.0** - Versão inicial com automação básica
- **v1.1.0** - Adicionado sistema de logs e screenshots
- **v1.2.0** - Implementada barra de progresso e relatórios

---

*Última atualização: Agosto 2025*