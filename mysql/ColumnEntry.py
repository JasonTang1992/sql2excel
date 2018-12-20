class ColumnEntry:

    def __init__(self, name, constraint, comment, dataType):
        self.name = name
        self.constraint = constraint
        self.comment = comment
        self.dataType = dataType

    def get_name(self):
        return self.__name


    def get_constraint(self):
        return self.__constraint


    def get_comment(self):
        return self.__comment


    def get_data_type(self):
        return self.__dataType


    def set_name(self, value):
        self.__name = value


    def set_constraint(self, value):
        self.__constraint = value


    def set_comment(self, value):
        self.__comment = value


    def set_data_type(self, value):
        self.__dataType = value


    def del_name(self):
        del self.__name


    def del_constraint(self):
        del self.__constraint


    def del_comment(self):
        del self.__comment


    def del_data_type(self):
        del self.__dataType

    name = property(get_name, set_name, del_name, "name's docstring")
    constraint = property(get_constraint, set_constraint, del_constraint, "constraint's docstring")
    comment = property(get_comment, set_comment, del_comment, "comment's docstring")
    dataType = property(get_data_type, set_data_type, del_data_type, "dataType's docstring")




