# -*- coding:utf-8 -*-
import re
import xlwt
import sys
from xlwt import *


class Entry(object):

    def __init__(self, name, typelength, default, comment):
        self.name = name
        self.typelength = typelength
        self.default = default
        self.comment = comment
        pass


class Styles(object):
    """docstring for Styles"""

    def __init__(self):
        super(Styles, self).__init__()
        self.goodstyle = XFStyle()
        self.poorstyle = XFStyle()
        self.normalstyle = XFStyle()

        pattern = Pattern()                 # 创建一个模式
        pattern.pattern = Pattern.SOLID_PATTERN     # 设置其模式为实型
        pattern.pattern_fore_colour = 0x2D
        # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 =
        # Yellow, 6 = Magenta,  the list goes on...
        self.poorstyle.pattern = pattern             # 将赋值好的模式参数导入Style

        fnt = Font()                        # 创建一个文本格式，包括字体、字号和颜色样式特性
        fnt.colour_index = 0x10                # 设置其字体颜色
        fnt.bold = False
        fnt.height = 12 * 20
        self.poorstyle.font = fnt  # 将赋值好的模式参数导入Style

        borders = Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        self.poorstyle.borders = borders  # 将赋值好的模式参数导入Style

        alignment = xlwt.Alignment()
        alignment.horz = 0x02      # 设置水平居中
        alignment.vert = 0x01      # 设置垂直居中
        self.poorstyle.alignment = alignment

        pattern = Pattern()                 # 创建一个模式
        pattern.pattern = Pattern.SOLID_PATTERN     # 设置其模式为实型
        pattern.pattern_fore_colour = 0x2A
        # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 =
        # Yellow, 6 = Magenta,  the list goes on...
        self.goodstyle.pattern = pattern             # 将赋值好的模式参数导入Style

        fnt = Font()                        # 创建一个文本格式，包括字体、字号和颜色样式特性
        fnt.colour_index = 0                # 设置其字体颜色
        fnt.bold = True
        fnt.height = 11 * 20
        self.goodstyle.font = fnt  # 将赋值好的模式参数导入Style

        borders = Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        self.goodstyle.borders = borders  # 将赋值好的模式参数导入Style

        alignment = xlwt.Alignment()
        alignment.horz = 0x02      # 设置水平居中
        alignment.vert = 0x01      # 设置垂直居中
        self.goodstyle.alignment = alignment

        pattern = Pattern()                 # 创建一个模式
        pattern.pattern = Pattern.SOLID_PATTERN     # 设置其模式为实型
        pattern.pattern_fore_colour = 1
        # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 =
        # Yellow, 6 = Magenta,  the list goes on...
        self.normalstyle.pattern = pattern             # 将赋值好的模式参数导入Style

        fnt = Font()                        # 创建一个文本格式，包括字体、字号和颜色样式特性
        fnt.colour_index = 0                # 设置其字体颜色
        fnt.bold = False
        fnt.height = 9 * 20
        self.normalstyle.font = fnt  # 将赋值好的模式参数导入Style

        borders = Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        self.normalstyle.borders = borders  # 将赋值好的模式参数导入Style

        alignment = xlwt.Alignment()
        alignment.horz = 0x02      # 设置水平居中
        alignment.vert = 0x01      # 设置垂直居中
        self.normalstyle.alignment = alignment

    def getStyle(self, style):

        if style == "poor":
            return self.poorstyle
        if style == "good":
            return self.goodstyle
        if style == "normal":
            return self.normalstyle
        return NULL


if __name__ == "__main__":

    style = Styles()

    book = xlwt.Workbook(encoding='utf-8',  style_compression=0)

    sql = open(sys.argv[1], "r")
    sql_content = sql.read().decode("utf-8")

    table_match = "CREATE TABLE\s+`\w+`\s+[^;]*"

    table_result = re.findall(table_match, sql_content)
    table_name_array = []

    for x in xrange(0, len(table_result)):
        table_content = table_result[x]
        table_name = ""

        tmp = re.findall(r'CREATE TABLE\s+`\w+`', table_content)
        tmp = re.findall(r'`\S+`', tmp[0])
        tmp = re.findall(r'[^`]+', tmp[0])
        table_name = tmp[0]
        table_name_array.append(table_name)

        entrys = re.findall("[^\n]*", table_content)
        entry_array = []
        print entrys
        for y in xrange(0, len(entrys)):

            tmp = re.findall("\S+", entrys[y])
            if len(tmp) == 0:
                continue
            tmp = re.findall("`\S+`", tmp[0])
            if len(tmp) == 0:
                continue

            print entrys[y]
            tmp = re.findall("`\S+`", entrys[y])
            # names.append(re.findall("[^`]+",tmp[0])[0])
            name = re.findall("[^`]+", tmp[0])[0]

            # types.append(re.findall("\S+", entrys[y])[1])
            typelength = re.findall("\S+", entrys[y])[1]

            tmp = re.findall("(NOT NULL)|(DEFAULT\s+\S+)", entrys[y])
            if len(tmp) != 0:
                # defaults.append(tmp[0])
                default = tmp[0]
                pass
            else:
                default = "NULL"

            tmp = re.findall("COMMENT\s+\'[^\']*\'", entrys[y])
            if len(tmp) != 0:
                tmp = re.findall("\'[^\']*\'", tmp[0])
                tmp = re.findall("[^\'']+", tmp[0])
                # comments.append(tmp[0])
                comment = tmp[0]
                pass
            else:
                comment = ""

            entry_array.append(Entry(name, typelength, default, comment))

            pass
        if len(table_name) > 30:
            table_name_tmp = table_name[0:30]
        else:
            table_name_tmp = table_name
        sheet = book.add_sheet(table_name_tmp.capitalize())
        sheet.write(0, 0, "序号", style.getStyle("good"))
        sheet.write(0, 1, "字段名", style.getStyle("good"))
        sheet.write(0, 2, "中文描述", style.getStyle("good"))
        sheet.write(0, 3, "类型（长度）", style.getStyle("good"))
        sheet.write(0, 4, "约束", style.getStyle("good"))
        sheet.write(0, 5, "是否敏感信息", style.getStyle("good"))
        sheet.write(0, 6, "备注", style.getStyle("good"))

        for i in xrange(0, len(entry_array)):
            sheet.write(i + 1, 0, x + 1, style.getStyle("normal"))
            sheet.write(
                i + 1, 1, entry_array[i].name.upper(), style.getStyle("normal"))
            sheet.write(i + 1, 2, "", style.getStyle("normal"))
            sheet.write(
                i + 1, 3, entry_array[i].typelength, style.getStyle("normal"))
            sheet.write(
                i + 1, 4, entry_array[i].default, style.getStyle("normal"))
            sheet.write(i + 1, 5, "N", style.getStyle("normal"))
            sheet.write(
                i + 1, 6, entry_array[i].comment, style.getStyle("normal"))

            pass

    sheet = book.add_sheet("表清单")

    sheet.write_merge(0, 0, 0, 6, "系统数据库表清单", style.getStyle("poor"))
    sheet.write(1, 0, "系统名", style.getStyle("good"))
    sheet.write(2, 0, "序号", style.getStyle("good"))

    sheet.write_merge(1, 1, 1, 4, "无忧服务", style.getStyle("good"))
    sheet.write(2, 1, "数据库名", style.getStyle("good"))
    sheet.write(2, 2, "数据库中文名", style.getStyle("good"))
    sheet.write(2, 3, "表名", style.getStyle("good"))
    sheet.write(2, 4, "中文名", style.getStyle("good"))

    sheet.write_merge(1, 1, 5, 6, "更新日期：", style.getStyle("good"))
    sheet.write(2, 5, "是否存在敏感字段", style.getStyle("good"))
    sheet.write(2, 6, "备注", style.getStyle("good"))

    for x in xrange(0, len(entry_array)):
        sheet.write(x + 3, 0, x + 1, style.getStyle("normal"))
        sheet.write(x + 3, 1, "", style.getStyle("normal"))
        sheet.write(x + 3, 2, "", style.getStyle("normal"))
        sheet.write(
            x + 3, 3, table_name_array[x].upper(), style.getStyle("normal"))
        sheet.write(x + 3, 4, "", style.getStyle("normal"))
        sheet.write(x + 3, 5, "N", style.getStyle("normal"))
        sheet.write(x + 3, 6, "", style.getStyle("normal"))
    book.save(sys.argv[1] + ".xls")
