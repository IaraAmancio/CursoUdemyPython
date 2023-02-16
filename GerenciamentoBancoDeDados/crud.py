"""
Consultas e alterações no banco de dados 'mydb' utilizando python e o SGBD MySQL Workbench

"""

import pymysql.cursors
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv() # retorna um dicionario com variaveis de ambiente

# context manager é utilizado para automatizar de forma adequada o fechamento de um recurso.
@contextmanager
def conecta():

    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password=os.environ["PASSWORD"],
        db=os.environ["DB"],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()

# inserir dados na tabela
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO agência (idAgência, Nome, salario_montante_total, cidade_agencia) VALUES (%s, %s, %s, %s)'
        dados = [
            (1,'abc',1000,'Brasil'),
            (2, 'abc', 2000, 'Brasil'),
            (3, 'abc', 3000, 'Brasil'),
            (4, 'abc', 4000, 'Brasil'),
        ]
        cursor.executemany(sql, dados)
        conexao.commit()

# deletar dados da tabela
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM agência WHERE idAgência = %s'
        cursor.execute(sql, (2,))
        conexao.commit()

# alterar dados da tabela
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE agência SET Nome = %s WHERE idAgência = %s'
        cursor.execute(sql, ('efg',1))
        conexao.commit()

# Consultas
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM agência WHERE salario_montante_total > 2000 ORDER BY salario_montante_total DESC')

        for linha in cursor.fetchall():
            print(linha['idAgência'], linha['salario_montante_total'])

