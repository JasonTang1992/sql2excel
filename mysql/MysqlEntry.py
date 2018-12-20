import pymysql

class MysqlEntry:
    
    def __init__(self, name, ip, port, username, password):
        self.name = name
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def get_name(self):
        return self.__name


    def get_ip(self):
        return self.__ip


    def get_port(self):
        return self.__port


    def get_username(self):
        return self.__username


    def get_password(self):
        return self.__password


    def set_name(self, value):
        self.__name = value


    def set_ip(self, value):
        self.__ip = value


    def set_port(self, value):
        self.__port = value


    def set_username(self, value):
        self.__username = value


    def set_password(self, value):
        self.__password = value


    def del_name(self):
        del self.__name


    def del_ip(self):
        del self.__ip


    def del_port(self):
        del self.__port


    def del_username(self):
        del self.__username


    def del_password(self):
        del self.__password

    name = property(get_name, set_name, del_name, "name's docstring")
    ip = property(get_ip, set_ip, del_ip, "ip's docstring")
    port = property(get_port, set_port, del_port, "port's docstring")
    username = property(get_username, set_username, del_username, "username's docstring")
    password = property(get_password, set_password, del_password, "password's docstring")
    
    