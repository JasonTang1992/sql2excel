class ColumnEnry:

    def __init__(self, name = "Unknown", constraint = Constraint(), comment = "", dataType = DataType() ):
        self.name = name
        self.constraint = constraint
        self.comment = comment
        self.dataType = dataType


class Constraint:

    def __init__(self, isKey = False, isNULL = True, default = ""):
        self.isKey = isKey
        self.isNULL = isNULL
        self.default = default

class DataType:

    def __init__(self, typeNum, length = 0, afterPoint = 0):
        self.typeNum = typeNum
        self.lenth = lenth
        self.afterPoint = afterPoint


