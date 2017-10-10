import pymysql # para o MySQL

con = pymysql.connect('127.0.0.1', 'root', '')
con.select_db('linarabot')

