'''
    Schema responsible for defining how routes return messages are
    displayed and also for routes parameters validation.
'''
from typing import Optional, List
import re
from datetime import datetime
from pydantic import BaseModel, validator
from model.email_sender import EmailSender

class EmailSentSchema(BaseModel):
    '''
        Define como será a resposta ao enviar um email de lembrete.
    '''
    message: str
    name: str
