'''
Created on 2018年12月18日

@author: jason
'''

from mysql import MysqlEntry

import pymysql
from mysql.DatabaseEntry import DataBaseEntry
from mysql.TableEntry import TableEntry

class MysqlUtil(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.name
        self.ip 
        self.port
        self.username
        self.password

        self.db
        self.cursor
        
    def connect(self, mysqlEntry = MysqlEntry()):
        # 打开数据库连接
        self.db = pymysql.connect(mysqlEntry.get_ip(), mysqlEntry.get_username(), mysqlEntry.get_password(), mysqlEntry.get_name())
         
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        
    def disconnect(self):
        self.db.close()
        
    def getDateDict(self):
        tables = []
        database = DataBaseEntry(self.name, tables)
        
        #获取表信息
        results = self.cursor.execute("SELECT * FROM " + self.name + "..sysobjects")
        
        #遍历表
        for row in results:
            #获取表的名称
            tableName = ""
            columns = []
            table = TableEntry(tableName, columns)
            
            #获取字段信息
            columns = 
        
        #遍历字段
        
        #获取字段属性
        
