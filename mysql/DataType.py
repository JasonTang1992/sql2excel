class DataType:

    def __init__(self, typeName = ""):
        self.typeName = typeName

    def get_type_name(self):
        return self.__typeName


    def set_type_name(self, value):
        self.__typeName = value


    def del_type_name(self):
        del self.__typeName

    typeName = property(get_type_name, set_type_name, del_type_name, "typeName's docstring")
