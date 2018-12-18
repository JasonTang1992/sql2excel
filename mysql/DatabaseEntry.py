from mysql import TableEntry

class DataBaseEntry:
    
    def __init__(self, name = "unknown", tables = []) :
        self.name = name
        self.tables = tables

    def get_name(self):
        return self.__name


    def get_tables(self):
        return self.__tables


    def set_name(self, value):
        self.__name = value


    def set_tables(self, value):
        self.__tables = value


    def del_name(self):
        del self.__name


    def del_tables(self):
        del self.__tables

    name = property(get_name, set_name, del_name, "name's docstring")
    tables = property(get_tables, set_tables, del_tables, "tables's docstring")

