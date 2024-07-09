'''Module responsible for routing at email sender'''
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from model import EmailSender
from model import Session
from logger import logger
from schemas import *

info = Info(title = 'Email sender API', version = '1.0.0')
app = OpenAPI(__name__, info = info)
CORS(app)

email_sender_tag = Tag(name = 'Rota de envio de Email', description = 'Envia um email de lembrete na sua criação ou atualização caso seja selecionada a opção.')

@app.post('/prepare', tags = [email_sender_tag])
def prepare():
    '''
        Esta rota envia um email com as informações do lembrete, ao email cadastrado.
    '''
    data = request.get_json()
    try:
        email_sender = EmailSender(
            name = data['name'],
            description = data['description'],
            due_date = data['due_date'],
            email_receiver = data['email_receiver']
        )
        email_sender.set_content(__check_flag(data['flag']))
        session = Session()
        session.add(email_sender)
        session.commit()
        EmailSender.send_email(email_sender)
        return {'mensagem': 'Email com informações do lembrete enviado para o destinatário: %s', 'email': email_sender.email_receiver}, 200
    except Exception as error:
        logger.warning('Erro ao validar e enviar email - erro : %s', error)
        return {'mensagem': 'Ocorreu um erro ao enviar o email.'}, 404

def __check_flag(flag) -> dict:
    flags = {
        'create': False,
        'update': False,
        'due_date': False
    }
    if flag in flags:
        flags[flag] = True

    return flags
