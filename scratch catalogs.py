import codecs
import pandas as pd
import openpyxl
wb=openpyxl.Workbook()#create a workbook to store the data
sheet=wb.active
f = codecs.open(r'C:/Users/jinha/Desktop/all.txt', mode='r', encoding='utf-8') # open txt files，and using‘utf-8'coding to read
line = f.readline() # read the file in row
list1 = []
while line:
    a = line.split()
    b = a[0:11] # choose the reading scope to read
    list1.append(b) # accumulation in list1
    line = f.readline()# read the file in row
for i in list1:
    sheet.append(i)#write in list1
wb.save('shenqi.xlsx')#store the data in a file
