import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )

    sql = """
    DROP DATABASE IF EXISTS rkwan;
    CREATE DATABASE hasan;
    USE hasan;
    CREATE TABLE one (
        age INT,
        name VARCHAR(255)
    )
    """

    mycur = conn.cursor()
    mycur.execute(sql, multi=True)
except mysql.connector.Error as err:
    print(err)
