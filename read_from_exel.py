import openpyxl

book = openpyxl.load_workbook('read_in_python.xlsx',read_only=True)

sheet = book.active
cells = sheet['B1':'C11']
for name,year in cells:
    print(name.value,year.value)

for row in range(1,sheet.max_row+1):
    author = sheet[row][0].value
    name = sheet[row][1].value

print(sheet['B1'].value)
print(sheet[1][2].value)