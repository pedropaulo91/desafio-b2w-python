# Desafio-B2W

## Uma API REST proposta como desafio para o processo seletivo.

Utilizei o micro web-framework Bottle para receber as requisições e o banco de dados SQLite.
O banco "database.db" já está populado com os planetas obtidos pela SWAPI. Para inicir o servidor,
basta digitar "python app.py" no prompt de comando na pasta do projeto. As requisições deve ser feitas
para "http://127.0.0.1:8000/planetas".

O módulo "baixar_planetas.py" faz requisições para cada um dos planetas da SWAPI e os insere no banco de dados.
Os dicionários retornados nas funções do módulo "main.py" são automaticamente convertidos para o formato JSON.

