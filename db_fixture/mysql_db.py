#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import setting

__author__ = 'YinJia'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymysql import connect, cursors
from pymysql.err import OperationalError
import configparser as cparser

# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG, encoding='UTF-8')
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
db = cf.get("mysqlconf", "db_name")



class DB:
    """
    MySQL基本操作
    """
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                # port=int(port),
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 查询表数据
    def get(self, table_name):
        """
        查询表数据
        :param table_name:
        :return:数据结果
        """
        get_sql = "select * from {}".format(table_name) + ';'
        cur = self.conn.cursor()
        cur.execute(get_sql)
        return cur.fetchall()

    # 插入表数据
    def insert(self, table_name, table_data):
        """
        :param table_name: 表名
        :param table_data: 插入数据：字典
        :return:
        """
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        res = None
        with self.conn.cursor() as cursor:

            try:
                res = cursor.execute(real_sql)
            except:
                pass
        self.conn.commit()
        if 1 != res:
            return 'failed'
        else:
            return 'success'

    # 删除表数据
    def clear(self, sql):
        """

        :param table_name:
        :return: failed：失败 success：成功
        """
        sql = sql
        # real_sql = "delete from " + table_name + ";"
        res = None
        with self.conn.cursor() as cursor:
            # 取消表的外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            res = cursor.execute(sql)
        self.conn.commit()
        if 0 != res:
            return 'failed'
        else:
            return 'success'

    # 关闭数据库
    def close(self):
        self.conn.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    # print(DB().get('student'))
    # token = {'sno': 12,
    #         'sname': '小哦',
    #         'sex': '男',
    #         'dept': 'php',
    #         'age': 20,
    #         }
    # print(DB().insert('student', table_data=token))
    #
    print(DB().get('t_foundation_operation'))
