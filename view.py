import sqlite3 as lite

conn = lite.connect('base.sqlite')

def insert(guia = '',nome_convenio = '',procedimento = '',valor = 0,quantidade = '',convenio = '', exportado = 0):
    with conn:
        valor_alterado = valor.replace(',', '.')
        dados = [guia,nome_convenio,procedimento,valor_alterado,quantidade,convenio, exportado]
        cursor = conn.cursor()
        query = "INSERT INTO lancamentos (n_guia, nome_convenio, procedimento, valor, quantidade, convenio, exportado) VALUES  (?,?,?,?,?,?,?)"
        cursor.execute(query, dados)




def monstrar_info():
    lista = []
    with conn:
        cursor = conn.cursor()
        query = "SELECT id,n_guia, convenio, nome_convenio, procedimento, valor, quantidade FROM lancamentos WHERE exportado=0"
        cursor.execute(query)
        info = cursor.fetchall()
        for i in info:
            lista.append(i)
        return lista
    

def monstrar_info_exportados():
    lista = []
    with conn:
        cursor = conn.cursor()
        query = "SELECT id,n_guia, convenio, nome_convenio, procedimento, valor, quantidade FROM lancamentos WHERE exportado=1"
        cursor.execute(query)
        info = cursor.fetchall()
        for i in info:
            lista.append(i)
        return lista
    


def atualizar_info(i):
    with conn:
        cursor = conn.cursor()
        query = f"UPDATE lancamentos SET n_guia=?, nome_convenio=?, procedimento=?, valor=?, quantidade=?, convenio=?, exportado=? where id=?"
        cursor.execute(query, i)


def deletar_lancamento(id_item):
    with conn:
        cursor = conn.cursor()
        query = "DELETE FROM lancamentos WHERE id=?"
        cursor.execute(query, id_item)
        
