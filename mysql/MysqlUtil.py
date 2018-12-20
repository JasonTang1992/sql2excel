'''
Created on 2018年12月18日

@author: jason
'''

import pymysql

from mysql.DatabaseEntry import DataBaseEntry
from mysql.TableEntry import TableEntry
from mysql.Constraint import Constraint
from mysql.DataType import DataType
from mysql.MysqlEntry import MysqlEntry
from mysql.ColumnEntry import ColumnEntry

class MysqlUtil(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name = ''
        self.ip  = ''
        self.port = ''
        self.username = ''
        self.password = ''
        self.db = ''
        self.cursor = ''
        
    def connect(self, mysqlEntry):
        # 打开数据库连接
        self.db = pymysql.connect(mysqlEntry.get_ip(), mysqlEntry.get_username(), mysqlEntry.get_password(), mysqlEntry.get_name())
         
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        
        self.name = mysqlEntry.get_name()
        
    def disconnect(self):
        self.db.close()
        
    def getDateDict(self):
        tables = []
        database = DataBaseEntry(self.name, tables)
        
        #获取表信息
        self.cursor.execute("show TABLES")
        tableResults = self.cursor.fetchall()
        
        #遍历表
        for table in tableResults:
            #获取表的名称
            tableName = table[0]
            columns = []
            tableEntry = TableEntry(tableName, columns)
            
            #获取字段信息
            self.cursor.execute(r"SELECT column_name, data_type, column_key, is_nullable, extra, column_default, column_comment FROM information_schema.`COLUMNS` WHERE table_schema = '" + self.name + r"' and table_name = '"+ tableName +r"'")
            columnResults = self.cursor.fetchall()
            
            #遍历字段
            for column in  columnResults:
                #获取字段属性
                
                #约束条件
                if(column[2] == 'PRI'):
                    primaryKey = True
                else:
                    primaryKey = False
                if(column[3] == 'YES'):
                    nullable = True
                else:
                    nullable = False
                if(column[4] == 'auto_increment'):
                    autoIncrement = True
                else:
                    autoIncrement = False
                default = column[5]
                constraint = Constraint(primaryKey, nullable, autoIncrement, False, default, [])
                
                #数据类型
                dataType = DataType(column[1])
                
                columnEntry = ColumnEntry(column[0], constraint, column[6] ,dataType)
                
                columns.append(columnEntry)
            #end for
            
            tables.append(tableEntry)
        #end for
        
        return database
            
        
       
        
        
        
