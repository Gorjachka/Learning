# # def fib(n):
# #     if n==1:
# #         return 0
# #     if n==2:
# #         return 1
# #     return fib(n-1)+fib(n-2)
# #
# # print(fib(7))
# p=[i for i in range (10)]
# fib=((lambda x :fib(x-1)+fib(x-2)) for x in range(10)  if x<=1)
# print (fib)
# # n=10
# # gen =(x for x in range(n))
# #
# # while gen<n:
# #
# #     print (fib((next(gen))))





file= open(("source.txt"), "r")   # (os.path.join(local_dir, "TableFinmon.txt"), "w") as file:
readfile=file.read().split('\n')
print (readfile)
lenth = len(readfile)
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
#
recur_fibo=lambda n: n if n<=1 else recur_fibo(n-1) + recur_fibo(n-2)

# check if the number of terms is valid
       # try:
       #     if lenth >0:
       #         fibo = ([recur_fibo(i) for i in range(lenth)])
       #         resultString = [i[::-1] for i in readfile if readfile.index(i) + 1 in fibo]
       #         for i in resultString:  # назад в стовбчик
       #             print(''.join(i))
       #
       # except NameError:
       #     print("Please enter some rows in a file")
       #else: print('qqqq')
fibo = ([recur_fibo(i) for i in range(lenth)])
resultString = [i[::-1] for i in readfile if readfile.index(i) + 1 in fibo]
print (resultString)
for i in resultString:  # назад в стовбчик
    print(''.join(i))#for i in resultString)

with open("myfilenew1.txt", "w+") as nefile:
    for i in resultString:

        nefile.write(f'{("".join(i))}\n')

    nefile.close()




# if lenth!= True:
#     fibo = ([recur_fibo(i) for i in range(lenth)])
#
# else:
#     print("Please enter some rows in a file")
   #print("Fibonacci sequence:")

   #print(fibo)

lenrow=([i.rfind(' ') for i in resultString]) #i[::-1].rfind(' ')
print((lenrow))
# for i in readfile:
#      print([t for t in i[:(lenrow)]])

reversed_row=[((i[(i.rfind(' ')+1):])) for i in resultString]
for count, value in enumerate(reversed_row, start=1):
    print(count, value)

#print(reversed_row.index('wor')) #for k in reversed_row])
print (reversed_row)
# for i in readfile:              #назад в стовбчик
#      print(''.join(i))


#print(readfile)
# resultString=[i[::-1] for i in readfile if readfile.index(i)+1 in fibo]
# for i in resultString:              #назад в стовбчик
#       print(''.join(i))
#
# f=(i for i in readfile)
# for k in f :
#     print(next(f)[::-1])


#     # for data in listeTableLoc35R:
#     file.write(tabulate())
#     file.close()