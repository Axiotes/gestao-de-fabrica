import pyodbc

class BancoDedados():
    def __init__(self, cursor=None):
        self.cursor = cursor

    def conectar(self):
        dados_conexao = (
            'Driver=SQL Server;'
            'Server=ARTHUR-AXIOTES;'
            'Database=gestao_de_fabrica;'
        )

        conexao = pyodbc.connect(dados_conexao)

        self.cursor = conexao.cursor()

    def addCliente(self, nomeCompleto, cpf, gmail, senha):
        comando = f"""insert into clientes
        (nomeCompleto, cpf, gmail, senha)
        values
        ('{nomeCompleto}', {cpf}, '{gmail}', '{senha}')"""

        self.cursor.execute(comando)
        self.cursor.commit()

    def conferirCadastro(self):
        comando = f"""select gmail, senha from clientes;"""

        return self.cursor.execute(comando).fetchall()