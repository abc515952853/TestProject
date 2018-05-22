import xlrd
import configparser

data = xlrd.open_workbook('E:\工作文档\汉画轩\测试用例.xls')
table = data.sheet_by_name('登录用例')
for i in range(table.nrows):
    nrows = table.row_values(i)
    print(table.col(0)[0].value)
config=configparser.ConfigParser()
config.read("config.ini")
mask=config.get("DATABASE",'host')
print(mask)