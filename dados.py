#banco de dados!
#feito com SQLITE3

import sqlite3

#criar e ativar database
dbase = sqlite3.connect('datafinance.db')
#pra utilizar o cursor
cursor = dbase.cursor()

#Nova tentativa de cursor
#cursor.execute("CREATE TABLE VS(entradas integer)")
def write_entrada(VE): 
    cursor.execute("INSERT INTO VE VALUES(?)", [VE])
    dbase.commit()


#cursor.execute("CREATE TABLE VS(saidas integer)")
def write_saida(VS): 
    cursor.execute("INSERT INTO VS VALUES(?)", [VS])
    dbase.commit()

def get_sum_entradas():
    cursor.execute("SELECT SUM(entradas) FROM VE")
    result = cursor.fetchone()[0]
    return result if result else 0

def get_sum_saidas():
    cursor.execute("SELECT SUM(saidas) FROM VS")
    result = cursor.fetchone()[0]
    return result if result else 0

#função que poe o valor na data base de valor total
#def write(VT):
 #   c.execute('''INSERT into datafinance(VT) VALUES(?)''',(VT))
  #  dbase.commit