##############################################################################
# Script envia e-mail via SMTP
# Idealizado por Robert Silva e adaptado por Kessi Diones (@kessix) 
# ################################################################################################

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Credenciais da conta de e-mail e servidor
email_from = 'Conta de E-mail'
email_password = 'Senha E-mail'
email_smtp_server = 'FQDN do Servidor SMTP'

# Pegando o horário so sistema
data = datetime.now()
data_string = data.strftime("%H:%M:%S - %d/%m/%Y") # formato da data e hora
print(data_string)

# Corpo do e-mail
destination = ['Conta de E-mail de Destino'] # e-mail de destino
subject = 'Título do E-mail'  # Assunto do e-mail
msg = MIMEMultipart() 
msg['From'] = email_from
msg['Subject'] = subject
text = "Mensagem do E-mail"
print(text)
msg_text = MIMEText(text, 'html')
msg.attach(msg_text)

# Configuração do servidor smtp
try:
    smtp = smtplib.SMTP(email_smtp_server, 587)
    smtp.ehlo()
    #smtp.starttls() - Usar se servidor tiver conexão TLS
    smtp.login(email_from, email_password)
    smtp.sendmail(email_from, ','.join(destination), msg.as_string())
    smtp.quit()
    print('Email enviado com sucesso')
except Exception as err:
    print(f'Falha ao enviar e-mail: {err}')
   
