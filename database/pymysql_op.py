# -*- coding: utf-8 -*-

"""
MYSQL操作(使用库 pymysql)
"""

from pymysql import Connection

# 构建mysql数据库连接
conn = Connection(
    host="localhost",   # 主机名
    port=3306,          # 端口
    user="root",        # 用户名
    password="123456"   # 密码
    # autocommit=True     # 设置事务自动提交
)

# 选择数据库
conn.select_db("python_test")

# 获取游标对象
cursor = conn.cursor()

# 执行语句
# cursor.execute("create table test(id int);")

# 执行查询语句
cursor.execute("select * from users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 执行写入语句
cursor.execute("INSERT INTO users(name, age) VALUES ('叶文洁', 36)")
# 提交事务(可通过连接参数 autocommit=true 设置自动提交)
conn.commit()


# 关闭连接
conn.close()
