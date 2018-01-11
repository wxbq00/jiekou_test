import xlrd
class Excel():
    def __init__(self,path,sheetName):
        self.data=xlrd.open_workbook(path)#打开表格
        self.table=self.data.sheet_by_name(sheetName)#获取表头
        self.keys=self.table.row_values(0)#第一行
        self.rowNum=self.table.nrows#总行数
        self.colNum=self.table.ncols#总列数
    def dict_data(self):
        if self.rowNum<=1:
            print('行数小于1')
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):#行数循环
                s={}
                values=self.table.row_values(j)#第二行开始
                for x in range(self.colNum):#列数循环
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r
if __name__ == '__main__':
    path='a.xlsx'
    sheetName='sheet1'
    data=Excel(path,sheetName)
    print(data.dict_data())

