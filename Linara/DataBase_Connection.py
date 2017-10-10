import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='linarabot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Executa a consulta na tabela selecionada
        cursor.execute("SELECT CHAVE FROM config;")
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

