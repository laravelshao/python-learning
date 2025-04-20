# -*- coding: utf-8 -*-

"""
MYSQL操作(使用官方库 mysql-connector-python)
"""

import mysql.connector


# 连接数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="python_test"
)

# 创建游标对象
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255),
                   age INT)''')

# 插入一条记录
sql = "INSERT INTO users(name, age) VALUES (%s, %s)"
val = ("Alice", 25)
cursor.execute(sql, val)
# 提交事务
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
for row in result:
    print(row)

# 关闭连接
cursor.close()
conn.close()