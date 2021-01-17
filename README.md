Script em python para envio de e-mails.

Script simples que pode ser integrado em servidores Linux, com suporte aos pacotes do Python.

Usei este script juntamente com o Cron do Linux para informar que as rotinas de backup do servidor tinham sido realizadas.

No entando, não existe limites para a aplicação desse script, pode integrado a outros, para criar processos mais elaborados de envios de e-mails em serviços automatizados, até mesmo com ferramentas DevOps como o Ansible.

Estou usando o módulo smtplib do python para estabelecer sessões SMTP cliente.

Para mais informações sobre esse módulo consulte a documentação disponível no site do python.org:
Link de acesso: https://docs.python.org/3/library/smtplib.html
