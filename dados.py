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

#função que poe o valor na data base de valor total
#def write(VT):
 #   c.execute('''INSERT into datafinance(VT) VALUES(?)''',(VT))
  #  dbase.commit