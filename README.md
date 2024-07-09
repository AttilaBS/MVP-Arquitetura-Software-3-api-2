# Lembretes api2

## Descrição do projeto:
   Este repositório faz parte das exigências da sprint Arquitetura de Software
  da pós graduação da PUC-Rio, curso Engenharia de Software, turma de julho de 2023.
  Neste repositório se encontra a API secundária que é responsável pela lógica de
  envio de emails e possui como funcionalidades: toda vez que recebe uma requisição
  da api1 para que envie email de um lembrete, primeiro persiste o email a ser
  enviado no banco de dados específico da api2 e, após, envia o email para o
  destinatário definido.

## Árvore de módulos. O sistema de pastas e arquivos do projeto está estruturado:
    api2
    |__ database
        |__ db.sqlite3
    |__ log
        |__ detailed.log
        |__ detailed.log1 ... .log10
    |__ model
        |__ __init__.py
        |__ base.py
        |__ email_sender.py
    |__ schemas
        |__ __init__.py
        |__ email_sender.py
        |__ error.py
    |__ .env(este arquivo não estará commitado, mas deve ser criado aqui)
    |__ .env.example
    |__ .gitignore
    |__ app.py
    |__ Dockerfile
    |__ logger.py
    |__ README.md
    |__ requirements.txt

## Como executar
   Para instruções detalhadas de como executar, verificar o README da api1.

## Responsabilidades dos arquivos do componente

## Pasta database:
  ### db.sqlite3
   Arquivo onde as operações no projeto são persistidas usando o banco
  de dados relacional SQLite.

## Pasta log:
  ### detailed.log
   Arquivo de log principal da aplicação, é um arquivo de texto
  responsável por armazenar informações de debug, erros e também sucesso
  mais genéricas.

  ### detailed.log1 ... .log10
   Arquivos de log com mais detalhes, com trace mais completo. Importantes
  para debug mais aprofundado.

## Pasta model:
  ### \_\_init\_\_.py
   Responsável por importar a lib de banco de dados, inicializá-lo,
  também por criá-lo na primeira execução do projeto e importar os demais
  models da aplicação.

  ### base.py
   Importa e inicializa a classe base que será usada nas operações no banco
  de dados.

  ### email_sender.py
   Model responsável pela persistência dos emails com seu respectivo template
  no banco de dados, bem como do envio ao destinatário.

## Pasta schemas:
  ### \_\_init\_\_.py
   Responsável por importar os schemas para a aplicação.

  ### email_sender.py
   Responsável por definir os padrões das respostas das rotas da aplicação,
  bem como validar o tipo de informação passada nas requisições.

  ### error.py
   Responsável por definir o padrão das respostas de erro da aplicação.

## Pasta raiz da aplicação:
  ### .env
   Arquivo responsável pelas variáveis de ambiente da aplicação. Não estará
  commitado por possuir informações sensíveis, mas deve ser criado ao se
  clonar a aplicação para que se consiga enviar emails, pois possuirá as
  variáveis de ambiente do servidor de emails.
  Obs.: Os valores das variáveis serão passados na entrega do MVP.

  ### .env.example
   Arquivo de exemplo, com o objetivo de ser referência dos nomes
  das variáveis de ambiente que devem ser passadas ao se criar o .env.

  ### .gitignore
   Responsável por adicionar arquivos e pastas que serão ignorados
  pelo sistema de versionamento do repositório.

  ### app.py
   Controlador da aplicação. Possui todas as rotas e lógica respectiva
  deste repositório, bem como responsável pelas rotas de comunicação
  com os demais serviços.

  ### Dockerfile
   Arquivo de configuração docker, específico para o serviço api2.

  ### logger.py
   Responsável pela configuração de logs da aplicação. Neste arquivo
  é possível customizar diversas opções de log, como o nível de disparo
  de log, formatação dos logs e etc.

  ### README.md
   Este arquivo. Responsável por descrever a aplicação, seus objetivos
  e instruções para execução.

  ### requirements.txt
   Possui as bibliotecas / módulos necessários para a execução correta
  da aplicação.
