import MySQLdb # para o MySQL

con = MySQLdb.connect('127.0.0.1', 'root', '')
con.select_db('linarabot')
