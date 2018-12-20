'''
Created on 2018年12月20日

@author: jason
'''
from mysql.MysqlUtil import MysqlUtil
from mysql import DatabaseEntry
from mysql.MysqlEntry import MysqlEntry
from mysql.TableEntry import TableEntry
from mysql import ColumnEntry

if __name__ == '__main__':
    
    mysql_aliyun = MysqlEntry("test", "39.98.70.211", "3306", "root", "pl,okm123")
    
    db = MysqlUtil()
    
    db.connect(mysql_aliyun)
    
    entry = db.getDateDict()
    
    print(entry.get_name())
    
    tables = entry.get_tables()
    
    for table in tables:
        print(table.get_name())
        for column in table.get_columns():
            print(column.get_name())
            print(column.get_data_type().get_type_name())
            print(column.get_constraint().get_primary_key())
            print(column.get_constraint().get_nullable())
            print(column.get_constraint().get_default())
            print(column.get_constraint().get_auto_increment())
            print(column.get_comment())
        
