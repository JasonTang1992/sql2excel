class Constraint:

    def __init__(self, primaryKey = False, nullable = True, autoIncrement = False, unique = False, default = "", foreginKey = []):

        self.primaryKey = primaryKey
        self.nullable = nullable
        self.default = default
        self.autoIncrement = autoIncrement
        self.unique = unique
        self.foreginKey = foreginKey

    def get_primary_key(self):
        return self.__primaryKey


    def get_nullable(self):
        return self.__nullable


    def get_default(self):
        return self.__default


    def get_auto_increment(self):
        return self.__autoIncrement


    def get_unique(self):
        return self.__unique


    def get_foregin_key(self):
        return self.__foreginKey


    def set_primary_key(self, value):
        self.__primaryKey = value


    def set_nullable(self, value):
        self.__nullable = value


    def set_default(self, value):
        self.__default = value


    def set_auto_increment(self, value):
        self.__autoIncrement = value


    def set_unique(self, value):
        self.__unique = value


    def set_foregin_key(self, value):
        self.__foreginKey = value


    def del_primary_key(self):
        del self.__primaryKey


    def del_nullable(self):
        del self.__nullable


    def del_default(self):
        del self.__default


    def del_auto_increment(self):
        del self.__autoIncrement


    def del_unique(self):
        del self.__unique


    def del_foregin_key(self):
        del self.__foreginKey

    primaryKey = property(get_primary_key, set_primary_key, del_primary_key, "primaryKey's docstring")
    nullable = property(get_nullable, set_nullable, del_nullable, "nullable's docstring")
    default = property(get_default, set_default, del_default, "default's docstring")
    autoIncrement = property(get_auto_increment, set_auto_increment, del_auto_increment, "autoIncrement's docstring")
    unique = property(get_unique, set_unique, del_unique, "unique's docstring")
    foreginKey = property(get_foregin_key, set_foregin_key, del_foregin_key, "foreginKey's docstring")

