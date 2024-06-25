'''Module responsible for routing at email sender'''
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from unidecode import unidecode
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from model import EmailSender
from model import Session
from logger import logger
from schemas import *

info = Info(title = 'Email sender API', version = '1.0.0')
app = OpenAPI(__name__, info = info)
CORS(app)

documentation_tag = Tag(name = 'Documentação', description = 'Seleção de documentação do envio de emails: Swagger')
email_sender_tag = Tag(name = 'Rota de envio de Email', description = 'Envia um email de lembrete na sua criação ou atualização caso seja selecionada a opção.')


@app.get('/send_email', tags = [documentation_tag])
def documentation():
    '''
        Redireciona para openapi, com a documentação das rotas da API.
    '''
    return redirect('/openapi')

@app.post('/prepare', tags = [email_sender_tag],
         responses = {'200': EmailSentSchema, '404': SentEmailErrorSchema})
def prepare(query: EmailSentSchema):
    '''
        Esta rota envia um email com as informações do lembrete, ao email cadastrado.
    '''
    logger.debug('chegou na api 2')
    email_sender = EmailSender(
        payload.name,
        payload.description,
        payload.due_date,
        payload.email_receiver)
    try:
        email_sender.prepare_and_send_email(flag_due_date = True)
        return {'mensagem': f'Email avisando do prazo final do lembrete enviado para o destinatário: {email_receiver}'}, 200
    except Exception as error:
        logger.warning('Erro ao validar e enviar email para lembrete# %d - erro : %s', reminder.id, error)
        return {'mensagem': 'Ocorreu um erro ao enviar o email.'}, 404
    # else:
    #     if not reminder.email_relationship[0].email:
    #         return {'mensagem': 'O lembrete não possui email cadastrado'}, 200
    #     if not reminder.send_email:
    #         return {'mensagem': 'O usuário optou por não receber email.'}, 200
