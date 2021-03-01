file = open('filename.txt','a+',encoding ='utf-8')
print (file.read())
file.seek(0)# перенос каретки на початок
print (file.readline())
for row in file:
    for letter in row:
        print(letter)
    #print(row)

s = file.readlines()
print(s)

file.write('hello')# перезаписує якщо режим 'r', 'a+' кидає в кінець

file.close()