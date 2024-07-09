'''Module responsible for email persistence, formatting and sending'''
import os
from email.message import EmailMessage
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
import ssl
import smtplib
from typing import Union
from dotenv import load_dotenv
from model import Base

load_dotenv('../.env')


class EmailSender(Base):
    '''Class representing an email_sender'''
    __tablename__ = 'send_email'

    id = Column('pk_email_sender', Integer, primary_key = True)
    name = Column(String(60))
    description = Column(String(255))
    due_date = Column(String(25))
    email_receiver = Column(String(255))
    subject = Column(String(255), default = 'Aviso de Lembrete')
    email_content = Column(String(1500), default = None)
    created_at = Column(DateTime, default = datetime.now())
    updated_at = Column(DateTime, default = None)

    def __init__(
        self,
        name: str,
        description: str,
        due_date: str,
        email_receiver: str,
        subject: str = 'Aviso de Lembrete',
        email_sender: str = os.environ.get('EMAIL_SENDER'),
        email_password: str = os.environ.get('APP_PASSWORD'),
        created_at: Union[DateTime, None] = None,
        updated_at: Union[DateTime, None] = None):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.email_receiver = email_receiver
        self.subject = subject
        self.email_sender = email_sender
        self.email_password = email_password

        if not created_at:
            self.created_at = created_at
        if not updated_at:
            self.updated_at = updated_at

    def set_content(self, flag):
        '''
            Function to create the email and send it.
        '''
        if flag['create'] or flag['update']:
            term = 'criado' if flag['update'] is False else 'atualizado'
            self.email_content = f'''
            <!DOCTYPE html>
                <html>
                    <body>
                        <h1 style="color:#2b89ad;">Lembrete:</h1>
                            <div><p>Olá usuário(a), este é um email automatizado
                            para avisar </br> que o lembrete nome: <strong>{self.name}</strong> 
                            </br> de descrição: <strong>{self.description}</strong>,
                            e com data final: <strong>{self.due_date}</strong>,
                            </br> foi {term}.</p>
                                <p>Atenciosamente,</p>
                                <p>Aplicativo Lembretes</p>
                            </div>
                    </body>
                </html>
            '''
        elif flag['due_date']:
            self.email_content = f'''
            <!DOCTYPE html>
                <html>
                    <body>
                        <h1 style="color:#2b89ad;">Lembrete:</h1>
                            <div><p>Olá usuário(a), este é um email automatizado
                            para avisar </br> que o lembrete nome: <strong>{self.name}</strong>
                            </br> de descrição: <strong>{self.description}</strong>,
                            e com data final: <strong>{self.due_date}</strong>,
                            </br> está próximo à data estipulada.</p>
                                <p>Atenciosamente,</p>
                                <p>Aplicativo Lembretes</p>
                            </div>
                    </body>
                </html>
            '''


    def send_email(self):
        message = EmailMessage()
        message.set_content(self.email_content, subtype = 'html')
        message['From'] = self.email_sender
        message['To'] = self.email_receiver
        message['Subject'] = self.subject
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, message.as_string())
