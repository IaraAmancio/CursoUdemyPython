# enviando e-mails SMTP com Python

import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv() # pega variáveis de ambiente de .env.

CAMINHO = Path(__file__).parent
CAMINHO_HTML = CAMINHO / 'email.html' # caminho para o arquivo.html.

# dados do remetente e destinatário
remetente = os.getenv("EMAIL_SENDER")
destinatario =os.getenv("EMAIL_RECIPIENT")

# configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv("EMAIL_SENDER", '')
smtp_password = os.getenv("EMAIL_PASSWORD", '')

# mensagem obtida do arquivo.html
with open(CAMINHO_HTML, 'r', encoding="utf-8") as arquivo:
    texto_html = arquivo.read()
    template = Template(texto_html)
    texto_email = template.substitute(nome = 'Iara')

# Cria contêiner de mensagem
mime = MIMEMultipart()
mime["from"] = remetente
mime["to"] = destinatario
mime["subject"] = 'Este é o assunto do e-mail.'

# Esta é a parte textual:
corpo_email = MIMEText(texto_email, "html", "utf-8")
# Anexa peças no contêiner de mensagem.
mime.attach(corpo_email)

with smtplib.SMTP(smtp_server,smtp_port) as server:
    # Cria uma instância no servidor SMTP
    server.ehlo() # Identifique-se em um servidor ESMTP
    server.starttls() # Todos os comandos SMTP a seguir serão criptografados
    server.login(smtp_user, smtp_password) # faz login em um servidor SMTP que exija autenticação
    server.send_message(mime) # envia e-mail
    print('Email enviado com sucesso!')



