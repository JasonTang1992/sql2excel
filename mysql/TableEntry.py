
class TableEntry:
    
    def __init__(self, name = "unknown", columns = []):
        self.name = name
        self.columns = columns

    def get_name(self):
        return self.__name


    def get_columns(self):
        return self.__columns


    def set_name(self, value):
        self.__name = value


    def set_columns(self, value):
        self.__columns = value


    def del_name(self):
        del self.__name


    def del_columns(self):
        del self.__columns

    name = property(get_name, set_name, del_name, "name's docstring")
    columns = property(get_columns, set_columns, del_columns, "columns's docstring")

