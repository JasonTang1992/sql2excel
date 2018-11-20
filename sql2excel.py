# -*- coding:utf-8 -*-
import re
import xlwt
import sys
from xlwt import *
import tkinter as tk
from tkinter import filedialog


class Entry(object):

    def __init__(self, name, typelength, default, comment):
        self.name = name
        self.typelength = typelength
        self.default = default
        self.comment = comment


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
        fnt.height = 9 * 20
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
        return

class SQLParser(object):
    """docstring for SQLParser"""
    def __init__(self):
        super(SQLParser, self).__init__()

    def parse(self, sql, excelpath):
        style = Styles()
        book = xlwt.Workbook(encoding='utf-8',  style_compression=0)
        table_match = "CREATE TABLE\s+`\S+`\s+[^;]*"
        table_result = re.findall(table_match, sql)

        table_name_array = []
        table_name_sheet = {}
        for x in range(0, len(table_result)):
            table_content = table_result[x]
            table_name = ""

            tmp = re.findall(r'CREATE TABLE\s+`\S+`', table_content)
            tmp = re.findall(r'`\S+`', tmp[0])
            tmp = re.findall(r'[^`]+', tmp[0])
            table_name = tmp[0]
            if table_name[0:29] in table_name_sheet:
                table_name_sheet[table_name[0:29]] += 1
                table_name = table_name[0:29] + str(table_name_sheet[table_name[0:29]])
            else:
                table_name_sheet[table_name[0:29]] = 0
                pass
            table_name_array.append(table_name)

            entrys = re.findall("[^\n]*", table_content)
            entry_array = []
            # print entrys
            for y in range(0, len(entrys)):

                tmp = re.findall("\S+", entrys[y])
                if len(tmp) == 0:
                    continue
                tmp = re.findall("`\S+`", tmp[0])
                if len(tmp) == 0:
                    continue

                # print entrys[y]
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
            # 计算列宽

            namelenmax = 10
            typelengthlenmax = 10
            defaultlenmax = 10
            commentlenmax = 10 
            for i in range(0, len(entry_array)):
                if len(entry_array[i].name) > namelenmax:
                    namelenmax = len(entry_array[i].name)
                if len(entry_array[i].typelength) > typelengthlenmax:
                    typelengthlenmax = len(entry_array[i].typelength)
                if len(entry_array[i].default) > defaultlenmax:
                    defaultlenmax = len(entry_array[i].default)
                if len(entry_array[i].comment) > commentlenmax:
                    commentlenmax = len(entry_array[i].comment)
            sheet.col(0).width = 400*(len("序号")+1)
            sheet.col(1).width = 400*(namelenmax+1)
            sheet.col(2).width = 400*(len("中文描述")+1)
            sheet.col(3).width = 400*(typelengthlenmax+1)
            sheet.col(4).width = 400*(defaultlenmax+1)
            sheet.col(5).width = 400*(len("是否敏感信息")+1)
            sheet.col(6).width = 400*(commentlenmax+1)

            sheet.write(0, 0, "序号", style.getStyle("good"))
            sheet.write(0, 1, "字段名", style.getStyle("good"))
            sheet.write(0, 2, "中文描述", style.getStyle("good"))
            sheet.write(0, 3, "类型（长度）", style.getStyle("good"))
            sheet.write(0, 4, "约束", style.getStyle("good"))
            sheet.write(0, 5, "是否敏感信息", style.getStyle("good"))
            sheet.write(0, 6, "备注", style.getStyle("good"))

            for i in range(0, len(entry_array)):
                sheet.write(i + 1, 0, i + 1, style.getStyle("normal"))
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

        for x in range(0, len(table_name_array)):
            sheet.write(x + 3, 0, x + 1, style.getStyle("normal"))
            sheet.write(x + 3, 1, "", style.getStyle("normal"))
            sheet.write(x + 3, 2, "", style.getStyle("normal"))
            sheet.write(
                x + 3, 3, table_name_array[x].upper(), style.getStyle("normal"))
            sheet.write(x + 3, 4, "", style.getStyle("normal"))
            sheet.write(x + 3, 5, "N", style.getStyle("normal"))
            sheet.write(x + 3, 6, "", style.getStyle("normal"))
        book.save(excelpath)

        return

class App(object):
    """docstring for App"""
    def __init__(self, master):
        super(App, self).__init__()
        self.fm1 = tk.Frame(master)
        self.openfiles = []
        self.savedir = ""
        self.unknowndir = 0

        self.openFiles = tk.StringVar()
        self.saveDir = tk.StringVar()
        self.progress = tk.StringVar()

        tk.Label(master, text = "SQL文件：").grid(row = 0, column = 0)
        tk.Entry(master, textvariable = self.openFiles).grid(row = 0, column = 1)
        tk.Button(master, text = "打开文件", command = self.selectPath).grid(row = 0, column = 2)

        tk.Label(master, text = "Excel文件：").grid(row = 1, column = 0)
        tk.Entry(master, textvariable = self.saveDir).grid(row = 1, column = 1)
        tk.Button(master, text = "保存文件", command = self.selectDir).grid(row = 1, column = 2)

        tk.Label(master, textvariable = self.progress).grid(row = 2, column = 0)
        tk.Button(master, text = "转换", command = self.convert).grid(row = 2, column = 2)

    def selectPath(self):
        self.openfiles = tk.filedialog.askopenfilenames(title = "打开SQL文件", filetypes = [('sql文件', '*.sql'), ('所有文件', '*')])
        if len(self.openfiles) > 0:
            self.openFiles.set(self.openfiles[0])
        

    def selectDir(self):
        self.savedir = tk.filedialog.askdirectory()
        self.saveDir.set(self.savedir)

    def convert(self):
        sqlparser = SQLParser()
        self.progress.set("转换开始")
        for sqlfilepath in self.openfiles:
            tmp = re.findall(r"\/([^ \f\n\r\t\v\/]+.)+\S+", sqlfilepath)
            tmp = re.findall("\S+.", tmp[0])
            if len(tmp)>0:
                filename = tmp[0]
            else:
                filename = "unknowndir" + str(self.unknowndir)
                self.unknowndir += 1
            self.progress.set(filename + " 开始转换")
            sqlfile = open(sqlfilepath, "r", encoding = 'utf-8')
            sqlparser.parse(sqlfile.read(), self.savedir + "/" + filename + ".xls")
            self.progress.set(filename + " 转换完成")
        self.progress.set("转换结束")
        

if __name__ == "__main__":

    root = tk.Tk()
    root.title("SQL2Excel")
    display = App(root)
    root.mainloop()
