#!usr/bin/env python
# -*- coding:utf-8 -*-
# __Author : Clark Qian



import xlwt
import datetime


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Weight Graph')

count = 0
#write in
for i in range(8):
    for j in range(10):
        worksheet.write(2*i+1,j,str((datetime.datetime.now()+datetime.timedelta(count+1)).date()))
        count += 1

for i in range(10):
    worksheet.col(i).width = 3000

workbook.save('test.xls')

# for i in range(72):
#     print((datetime.datetime.now()+datetime.timedelta(i)).date())
