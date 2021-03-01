# # x = int(input());
# # if x >= 60 and x <= 720:
# #     print(int(x // 60))
# #     print(int(x % 60))
# # elif x <= 60:
# #     print(int(x // 100))
# #     print(int(x % 100))
# # elif x > 720:
# #     print('Error :  time more era')
#
# # x = int(input());
# # h = int(input());
# # m = int(input());
# # print ((x + h*60 + m)//60)
# # print ((x + h*60 + m)%60)
#
#
# # n = int(input());
# # if 1900 <= n <= 3000 and\
# #        (n%4==0 and n%100!= 0 or n%400==0):
# #   print("Високосный")
# # else:
# #    print("Обычный")
#
# # a = int(input());
# # b = int(input());
# # c = int(input());
# # p = (((a + b + c) / 2));
# # s = (p * (p - a) * (p - b) * (p - c))
# # print(s ** 0.5)
#
# # a = int(input());
# # if (12 >= a > -15):
# #     print('True')
# # elif (17 > a > 14):
# #     print('True')
# # elif a >= 19:
# #     print('True')
# # else:
# #     print('False')
#
# # x = int(input())
# # print (-15 < x <= 12 or 14 < x < 17 or 19 <= x)
#
# # a = float(input());
# # b = float(input());
# # c = str(input());
# # if c ==  "+":
# #     print (a+b)
# # elif c == "-":
# #     print (a-b)
# # elif c == "mod" and b != 0:
# #     print (a%b)
# # elif c == "div" and b != 0:
# #     print(a//b)
# # elif c == "*":
# #     print (a*b)
# # elif c == "pow":
# #     print (a**b)
# # elif (c == "/" or c =="mod" or c == "div") and b == 0 :
# #     print("Деление на 0!")
# # elif c == "/" and b != 0 :
# #     print(a/b)
# #
# #
# # a = float(input())
# # b = float(input())
# # act = input()
# #
# # if (act=="/" or act=="mod" or act=="div") and b==0:
# #     c = "Деление на 0!"
# # elif act=="+":    c = a + b
# # elif act=="-":    c = a - b
# # elif act=="/":    c = a / b
# # elif act=="*":    c = a * b
# # elif act=="mod":  c = a % b
# # elif act=="pow":  c = a ** b
# # elif act=="div":  c = a // b
# #
# # print (c)
#
#
# # a = float();
# # b = float();
# # c = float();
# # r = float();
# # d = str(input());
# # p = 0
# # if d == "треугольник":
# #     a = float(input());
# #     b = float(input());
# #     c = float(input());
# #     p = (((a + b + c) / 2));
# #     print ((p * (p - a) * (p - b) * (p - c))**0.5)
# # elif d == "прямоугольник":
# #     a = float(input());
# #     b = float(input());
# #     print(a*b)
# # elif d == "круг":
# #     r = float(input());
# #     print (3.14*r**2)
# # else:
# #     print ("none")
#
# # a = int(input());
# # b = int(input());
# # c = int(input());
# # line1 = max(a,b,c);
# # line2 = min(a,b,c);
# # line3 = (a+b+c) - line1 - line2
# #
# # print(line1,'\n', line2,'\n', line3)
#
# # a = input(range(0,1000));
# # b = 'программист'
# # c = 'ов'
# # f = 'а'
# # #if ( '0' <= a <= '1000'):
# #     #print('Error: a is not in range (0:1000)')
# # #else:
# #         if (a[(len(a) - 1)] == 0) \
# #         or ('9' >= a[(len(a) - 1)] >= '5') \
# #         or (('14' >= a >= '11')
# #             or ('14' >= a[(len(a) - 2):] >= '11')):
# #             print(a, (b + c))
# #         elif (a[(len(a) - 1)] == '1'):
# #          print(a, b)
# # #elif '0' <= a <= '1000':
# #     #print('Error: a is not in range (0:1000)')
# #         else:
# #             print(a, (b + f))
#
# # a = int(input());
# # if 0 <= a <= 1000:
# #     if 5 <= a % 100 <= 9 or
# #         5 <= a % 100 <= 9 or 11 <= a <= 14 or 11 <= a % 10 <= 14 or a == 0:
# #     print(a, 'программистов')
# #     elif a % 100 == 1:
# #      print(a, 'программист')
# #     else:
# #         print(a, 'программиста')
# # else:
# # print('Error: a is not in range (0:1000)')
# #
# # # elif 11 <= a%100 <= 14:
# # # print(a, 'программистов')
#
#
# # x = int()
# # if a != 0 and b != 0:
# #     if a // b == 0:
# #         x = a;
# #     elif b // a == 0:
# #         x = b
# #
# #     if a != b:
# #         x = a + b;
# #     else: x = a
# #
# #     while x%a != 0 or x%b != 0 or (a//b == 0 or b//a ==0):
# #          x = x + 1;
# #
# #     print (x)
# # else:
# #     print (a+b)
# # i = min(a, b)
# # if a != 0 and b != 0:
# #     while True:
# #      if i%a==0 and i%b==0:
# #             break
# #     i += 1
# #     print(i)
# # else:
# #     print (a+b)
#
# #                                  найменше спільне кратне
# # def lcm(a,b):
# #     m = a * b
# #     while a != 0 and b != 0:
# #         if a > b:
# #             a %= b
# #         else:
# #             b %= a
# #     return m // (a + b)
# #
# # while 1:
# #     try:
# #         x = int(input())
# #         y = int(input())
# #         print(lcm(x, y))
# #     except:
# #         break
#
#
# # x = int();
# # while x < 100:
# #     x = int(input())
# #     if x >= 10 and x < 100:
# #         print(x)
# #         continue
# #     if x >= 100 :
# #             break
#
#
# # x = int(input());
# # while x < 100:
# #     x = int(input())
# #     if x < 10 or x >= 100:
# #              continue
# #     else:
# #         print(x)
# #     if x >= 100 :
# #             break
# # n=int(input('5'));
# # m=int(input('6'));
# # a=int(input('7'));
# # b=int(input('9'));
# # x=0;
# # y=0;
# # for j in range(5,6+1):
# #     print('\t',j,end='')
# #
# # for i in range(7,9+1):
# #     print('\n',i,end='')
# #     for x in range (5,6+1):
# #         x=i*j
# #         print('\t',x,end='')
# #         for x in range(6,5):
# #             x = i * j
# #             print('\t', x, end='')
# # for y in range (7,9+1):
# #  y=5*i
# #  print('\t',y,end='')
#
#
# # n=int(input())
# # m=int(input());
# # for i in range(n):
#
# # for j in range(n):
# #     print(j,end='\t')
# # print()
#
# ##############################################
# # s=input('')
# # #a=s.upper()count('g'.upper());
# # #b=s.upper()count('c'.upper());
# # #x=(a+b)/len(s)*100
# # print((s.upper().count('g'.upper())+s.upper().count('c'.upper()))/len(s)*100)
# ############################################
# # s = 'abcdefghijk'
# # print (s[3:6],s[:6],s[3:],s[::-1],s[-3:],s[:-6],s[-1:-10:-2])
#
# # s = 'ZZZzppz'
# # i = 0
# # q = -1
# # j = len(s)-1
# # k = 0
# # n = 1
# # a = 0
# # b = 0
# # #while s[i] != s[j] and s[n] != s[j]:
# # while s[i] == s[n] or s[i] == s[q]and s[n] != s[j]:
# #             # k= n+1
# #
# #             a = (s[:j] + '0' + s[j + 1:])
# #             n += 1
# #             q += 1
# #             #print(s.count(a), a)
# # # else:
# # #
# # #             #print(s.count(a), a)
# # #             i += 1
# # #             n = 1
# # #             b = (s[i])
# # #            # print(b[0], n)
# #
# # if (q > 1 and s[i] != '0'):
# #                  print(s[i],i)
# # for i in b:
# # print(s.count(b),b)
#
#
# # print(k)
# # print(a)
# # print(b)
# # string = "ZZZxxz";
# # f=str()
# # Counts each character present in the string
# # for i in range(0, len(string)):
# #       c = 1;
# #       for j in range(i + 1, len(string)):
# #             if (string[i] == string[j] and string[i] != ' '):
# #                   c = c + 1;
# #                   # Set string[j] to 0 to avoid printing visited character
# #                   string = string[:j] + '0' + string[j + 1:];
# #
# #                   # A character is considered as duplicate if count is greater than 1
# #       if (c > 1 and string[i] != '0'):
# #             print(c,string[i]);
#
# # students = ['Ivan', 'Masha', 'Sasha']
# # students += ['Olga']
# # students += 'Olga'
# # print(students)
# ####################################################################
# # a = [1,2,3,4,5,6]
# # a = [int(i) for i in input().split()]
# # f = [0] * len(a)
# # b.pop(0)
# # b.append(a[0])
# # c = a.copy()
# # c.insert(0, a[-1])
# # c.pop(-1)
# # if len(a) > 1:
# #     f = [b + c for b, c in zip(b, c)]
# #     f = ' '.join(map(str, f))
# #     print(f)
# # else:
# #     a = ' '.join(map(str, a))
# #     print(a)
# #######################################################################
# # z = [4, 8, 0, 3, 4, 2, 0, 3]
# # z = [int(i) for i in input().split()]
# # a=[0]
# # z.sort()
# # a=[x for x in z if z.count(x) >= 2]
# # a=[a[i] for i in range(len(a)) if i == a.index(a[i])]
# # a = ' '.join(map(str, a))
# # print(a)
# ######################################################################
# # a= [int(i) for i in input()]
# #
# # while sum(a[i])!=0 :
# #     for i in a:
# #         i+=int(input())
# # else:
# #     a=[int(i)**2 for i in a]
# #     print(a)
#
# #######################################################################
# # def func(x):
# #     if x <= -2:
# #         return 1-(x+2)**2;
# #     elif -2<x<=2:
# #         return  -x/2;
# #     elif 2<x:
# #         return (x-2)**2+1
# # a=float(input())
# # print (func(a))
# #######################################################################
# # def modify_list(l):
# #     #l = [int(i) for i in l]
# #     for i in l:
# #        if i % 2 != 0:
# #             i = l.index(i);
# #             l.pop(i);
# #             #break
# #        elif i%2==0:
# #            l.append(i // 2)
# #            i = l.index(i);
# #            l.pop(i);
# #
# #     #print(l)
# #
# #
# # lst = [10, 5, 8, 3]
# # modify_list(lst)
# # print(lst)
#
#
# #
# # def update_dictionary(d, key, value):
# #     #d = {int(key):str(value)}
# #     if key in d:
# #        # d.update({key: value})
# #        # d.get(key,value)
# #         d = {int(key): str(value)}
# #         return d
# #     elif 2 * key in d:
# #             d.update({2*key: value})
# #             return d
# #     else:
# #             d = {2 * key, value}
# #
# #
# # d = {}
# # print(update_dictionary(d, 1, -1))  # None
# # print(d)                            # {2: [-1]}
# # update_dictionary(d, 2, -2)
# # print(d)                            # {2: [-1, -2]}
# # update_dictionary(d, 1, -3)
# # print(d)                            # {2: [-1, -2, -3]}
#
# ##############################################################
# # s = str(input().lower().split())
# # for i in s:
# #     if i==i+1:
# #         print(count(i))
# #     else:
# #         i+=1
# #         print(i)
# ##############################################################
# # from math import pi
# # # r=int(input())
# # # print(pi*r*2)
# ##############################################################
# # import requests
# # r= requests.get('https://stepic.org/media/attachments/course67/3.6.2/383.txt')
# # print(r.text)
# # print(r.__sizeof__())
# ################################################################
# ######################GENERATOR INPUT!!!!!!!!!!!!!!!!!!!
# # m = int(input())
# # n = [int(input()) for i in range (m)]
# # print(sum(n))
# # OR
# # print(sum([int(input()) for _ in range(int(input()))]))
# #################################################################
# # x=[1,2,3]
# # print(id(x))
# # print(id([1,2,3])) ##############different id numbers
# #################################################################
# # x = [1, 2, 3]
# # y = x
# # y.append(4)
# #
# # s = "123"
# # t = s
# # t = t + "4"
# #
# # print(str(x) + " " + s)##############differernt link to object
# ################################################################
# # count=0
# # #obj=[1, 2, 1, 2, 3]
# # objects = [1, 2, 1, 2, 3,'false',[],'pppp'] #in range(0,100)]
# # a=[]
# # for i in objects:
# #      if id(i) in objects:
# #         a.append(i)
# # #         ans+=1
# #         print(len(a))
# # ans=[[i,objects.count(i)] for i in set(i)]
#
#
# # def countList(lst, x):
# #     count = 0
# #     for i in lst:
# #         x = id(i)
# #         if x in lst[i]:
# #             count += 1
# #
# #     return count
# # x=int()
# # print(countList(list,x))
# #######################################
# # def closest_mod_5(x):
# # if x % 5 == 0:
# #     return x
# # return (x + 5 - x%5)
# #######################################
# # class MoneyBox:
# #     def __init__(self, capacity):
# #         self.capacity=capacity
# #    # конструктор с аргументом – вместимость копилки
# #     def can_add(self, v):
# #         if v<capacity:
# #             return True
# #         # True, если можно добавить v монет, False иначе
# #
# #     def add(self, v):
# #         if v<capacity is True:
# #             capacity+=v
# #
# #
# # money=MoneyBox(10)
# # money.add(5)
# ###########################################
# # def foo(x,y):
# #     try:
# #         return x/y
# #     except (TypeError, ZeroDivisionError) as e:
# #         print(type(e))
# #         print(e)
# #         print(e.args)
# #
# # print(f(5,0))
# ###############################################
# # ієрархія помилок
# # try:
# # #     foo()
# # # except ZeroDivisionError:
# # #     print("ZeroDivisionError")
# # # except ArithmeticError:
# # #     print("ArithmeticError")
# # # except AssertionError:
# # #     print("AssertionError")
#
# # try:
# #     foo()
# # except (ZeroDivisionError, AssertionError) as e:
# #     print(e.__class__.__name__)
# # except:
# #     print('ArithmeticError')
# #############################################
# # class Bad_name(Exception):
# #     pass
# #
# # def greet(name):
# #     if name[0].isupper():
# #         return "Hello, "+ name
# #     else:
# #         raise Bad_name(name+" is inappropriate name")
# #
# # print(greet("Andriy"))
# # print(greet("andriy"))
# ####################################################
# # class NonPositiveError(Exception):
# #     pass
# # class PositiveList(list):
# #
# #     def append(self,x):
# #         self.x=x
# #         if x > 0:
# #             super().append(x)
# #         else:
# #             raise NonPositiveError
# #
# # add=PositiveList()
# # add.append(2)
# # add.append(3)
# # print(add)
# ###################################################
#
# # from datetime import datetime
# # from datetime import timedelta
# # date=input()
# # date = datetime.date(date)
# # days=datetime.timedelta(input())
# # print(date.year)
# ###################################################
# # import simplecrypt
# ##################################################
# # lst=[1,2,3]
# # book={
# #     'title': 'The LangoLiers',
# #     'author': 'Stepnen King',
# # }
# # string="hello,world!"
# #
# # for i in book:
# #     print(i)
# #
# # it= iter(book)#ітератор для створення власної ітерації класів
# # while True:
# #     try:
# #         i=next(it)
# #         print(i)
# #     except StopIteration:
# #         break
# #######################################################
# # class Random_iterator:
# #     def _next_(self):
# #         return 0
# #
# # x= Random_iterator()
# # print(next(x))
# ##########################################################
# # book={
# # #     'title': 'The LangoLiers',
# #     'author': 'Stepnen King',
# # }
# # for i in book:
# #     print(i)
# #
# # it=iter(book)# робта for виражена через iter-next
# # while True:
# #     try:
# #         i=next(it)
# #         print(i)
# #     except StopIteration:
# #         break
# ##################################################################
# # ctr=0
# # # # while True: #опис роботи циклу While true
# # # #     inp=input("input a number")
# # # #     inp = int (inp)
# # # #     if (inp!=ctr):
# # # #         print ("didn't enter that number yet")
# # # #     elif(inp==ctr):
# # # #         print("ok")
# # # #         break
# # i = 0
# # while True:
# #     i += 1
# #     if i == 12:
# #         break
# #     print (i)
# ######################################################################
# # from random import random
# # class Random_iterator:
# #     #виводить довільне число потрібну кількість разів
# #     def __iter__(self):
# #         return self
# #
# #     def __init__(self,k):
# #         self.k=k
# #         self.i=0
# #
# #     def __next__(self):
# #         if self.i < self.k:
# #             self.i+=1
# #             return random()
# #         else:
# #             raise StopIteration
# #
# # for x in Random_iterator(10):
# #     print(x)
# #######################################################################
# # генератор yield
# # def simple_gen():
# #     print('Chekpoint 1')
# #     yield 1
# #     print('Chekpoint 2')
# #     yield 2
# #     print('chekpoint 3')
# #
# # gen=simple_gen()
# # x=next(gen)
# # print(x)
# # y=next(gen)
# # print(y)
# #######################################################################3
# # f=open('misc.xml')
# # x=f.read(5)
# # print(x)
# #
# #
# #
# # f.close()###################
# # def greet(name, owner):
# #     name = str(input());
# #     owner = str(input());
# #     if name == owner:
# #         print("Hello boss");
# #     else:
# #         print("Hello quest");
# #
# # print(greet())###################
#
# # n = int(input())
# # for i in range(n):
# #     for J in range(n):
# #         print('*',end='')
# #     print()
# ######################################
# # a= int(input())
# # b= int(input())
# # c= int(input())
# # d= int(input())
# # for k in range(1,2):
# #     for l in range (c, d + 1):
# #         print('\t',l,end='')
# #
# # for i in range(a,b+1):
# #
# #     print('\n',i,end='\t')
# #     for j in range(c,d+1):
# #         print('',i*j,end='\t')
# #     print()
# # def century(year):
# #     return year//100 if year%100 == 0 else year//100 + 1
# #
# # print(century(1900))
#
# #  def monkey_count(n):
# #     l =[i for i in range (1,n+1)]
# #     return l
# #     #your code here
# # print(monkey_count(10))
#
#
# # def maps(a):
# #     n = list(map(lambda x: x*2,a))#############use map & lambda
# #     return n
# # print(maps([1, 2, 3]))
#
# # def invert(lst):
# #     return list(map(lambda x: x * -1, lst))
# #
# # print(invert([1,2,3,4,5]))
#
# # def find_smallest_int(arr):############## use MIN
# #     return min(arr)
# #
# # print(find_smallest_int([78, 56, 232, 12, 11, 43]))
#
# # def well(x):
# #     count =  x.count('good')
# #     if count <= 2:
# #         return 'Publish!'
# #     elif count > 2:
# #         return 'I smell a series!'
# #     else :
# #          return 'Fail!'
# #
# # print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
# #
# # def count_positives_sum_negatives(arr):
# #     pos_count, neg_count = 0, 0
# #     if len(arr)>0 :
# #         for i in arr:
# #             if i > 0:
# #                 pos_count +=1
# #             elif i == 0:
# #                 pos_count = 0
# #
# #             else:
# #                 neg_count += i
# #
# #         d = (pos_count, neg_count)
# #         return list(d)
# #     else:
# #         return list([])
# #
# #
# # def count_positives_sum_negatives(arr):
# #     if not arr: return []
# #     pos = 0
# #     neg = 0
# #     for x in arr:
# #       if x > 0:
# #           pos += 1
# #       if x < 0:
# #           neg += x
# #     return [pos, neg]
# # print(count_positives_sum_negatives([]))
#
# # def abbrevName(name):################### capilize letter, find by gap
# #     return name[:1].title() + "." + name[name.find(' ')+1].title()
# #
# # print(abbrevName("sam harris"))
#
# # def nth_even(n):
# #     l =[int(i) for i in range (0,n*2,2)];
# #     return l[-1:n] ##################slice
# #
# # print(nth_even(200))
# #
# # def solution(string):
# #    return string[::-1]
# #
# # print(solution('world'))
#
# # def divisible_by(numbers, divisor):
# #     return [i for i in numbers if i % divisor == 0]
# #
# # print(divisible_by([1,2,3,4,5,6], 2))
#
# # def expression_matter(a, b, c):
# #     max1 = a*(b+c);
# #     max2 = a*b*c;
# #     max3 = a+b*c;
# #     max4 = (a+b)*c;
# #     max5 = a+b+c;
# #     return max(max1, max2 ,max3, max4,max5)
# #
# # print(expression_matter(1, 1, 1))
#
# # def calculate_tip(amount, rating):
# #     rating = rating.casefold()
# #     if rating == 'Terrible'.casefold():
# #         a = amount*0;
# #     elif rating =='Poor'.casefold():
# #         a = amount * 0.05;
# #     elif rating == 'Good'.casefold():
# #         a =  amount * 0.1;
# #     elif rating == 'Great'.casefold():
# #         a =  amount* 0.15;
# #     elif rating == 'Excellent'.casefold():
# #         a = amount * 0.2;
# #     else:
# #         return ('Rating not recognised');
# #     return round(a)
# #
# # print(calculate_tip(107.65, "GReat")
# #
# # def calculate_tip(a, r):
# #     d = {'terrible': 0,'poor': .05,'good': .10,'great': .15,'excellent': .20} ##########словник {} dict
# #     return int(d[r.lower()] * a + .99) if r.lower() in d else 'Rating not recognised'
#
# # def sum_list_items(ls):
# #   # return [sum(i) for i in range(ls)]
# #     return sum(i for i in ls)
# # ls = [2]
# # print (sum_list_items(ls))
#
# # def get_unique_items(ls):
# #     # x = []
# #     # # for i in ls:
# #     # #     if i not in x:
# #     # #         # x.append(i)
# #     # # return x
# #     return list(set(ls))
# # print(get_unique_items([1, 2, 3, 3, 3, 3, 4, 5]))
# # def is_palindrome(string):
# #     string = str(())
# #     a = string[::-1]
# #     if string == a:
# #       return True
# #
# # print (is_palindrome(mamam))
#
# # def is_palindrome(string):     POLINDROM
# #   while string == string[::-1] and string != '':   #reversed string
# #     return True
# #     break
# #   else:
# #       return False
#
# # def get_three_largest(ls):
# #         # k = sorted([len(i) for i in ls]);
# #         # return [i for i in k[2::1]]
# #     for i in ls:
# #         if len(i) == max(ls):
# #             return  i
# #         else:
# #
# #
# # print (get_three_largest(['kklllllllkk','k','llllllll','llllllllllll','omoooo']))
#
#
# # def decode_morse(message):
# #     MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
# #                        'C': '-.-.', 'D': '-..', 'E': '.',
# #                        'F': '..-.', 'G': '--.', 'H': '....',
# #                        'I': '..', 'J': '.---', 'K': '-.-',
# #                        'L': '.-..', 'M': '--', 'N': '-.',
# #                        'O': '---', 'P': '.--.', 'Q': '--.-',
# #                        'R': '.-.', 'S': '...', 'T': '-',
# #                        'U': '..-', 'V': '...-', 'W': '.--',
# #                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
# #                        '1': '.----', '2': '..---', '3': '...--',
# #                        '4': '....-', '5': '.....', '6': '-....',
# #                        '7': '--...', '8': '---..', '9': '----.',
# #                        '0': '-----', ', ': '--..--', '.': '.-.-.-',
# #                        '?': '..--..', '/': '-..-.', '-': '-....-',
# #                        '(': '-.--.', ')': '-.--.-'}
# #
# #
# #
# #         # extra space added at the end to access the
# #         # last morse code
# #         message += ' '
# #
# #         decipher = ''
# #         citext = ''
# #         for letter in message:
# #
# #             # checks for space
# #             if (letter != ' '):
# #
# #                 # counter to keep track of space
# #                 i = 0
# #
# #                 # storing morse code of a single character
# #                 citext += letter
# #
# #                 # in case of space
# #             else:
# #                 # if i = 1 that indicates a new character
# #                 i += 1
# #
# #                 # if i = 2 that indicates a new word
# #                 if i == 2:
# #
# #                     # adding space to separate words
# #                     decipher += ' '
# #                 else:
# #
# #                     # accessing the keys using their values (reverse of encryption)
# #                     decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
# #                                                                   .values()).index(citext)]
# #                     citext = ''
# #
# #         return decipher
# # print(decode_morse(['s o s']))
#
# # def high_and_low(numbers):
# #
# #     #k = set[numbers]
# #     return sorted(numbers)#k[0::1]
# #
# # print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
# # a = int(input())
# # b = int(input())
# # print("a+b =",a+b,'\n',"a-b =",a-b,'\n',"a*b =",a*b,'\n',"a/b =",round(a/b,2),'\n')
#
# # import this
# # a,b =b,a
#
# # a=int(input('enter number:'))# більше менше
# # b=int(input('enter number:'))
# # while a!=b:
# #     print(f'{a}>{b}' if a>b else f'{b}>{a}')
# #     break
# # else:
# #     print (f'{a}={b}')
#
#
# # def reverse(st):
# #
# #     st=st.split(',')
# #     st=st[::-1]
# #     for i in st :
# #         if i != ' ':
# #          st = ' '.join(st)
# #     else:
# #         pass
# #
# #     return st
# #
# # print(reverse('wer      too'))
# # a=0
# # while a <=98 :
# #     a+= 2
# #     print(a)
# # i=0
# # for i in range (101):
# #     print(i if i%2==0 and i!=0 else '')
# # a=1
# # while a <=99 :
# #     a+=1
# #     print( a if a%2!=0 else '')
# # #
# # a=0
# # while a in range(10):
# #     a += 1
# #     #print (a if a%2==0 and a//2 != 0 else '')
# #     print(a if a % 2 != 0 and a // 3 != 0 else '')
# #     continue
#
# # check_list=[2,4,8]
# # for i in check_list:
# #     while i%2!=0:
# #         print("знайдено непарне число")
# #         break
#
# # number_factorial = int(input('enter factorial of the number:'))
# #
# # factorial = 1
# # while number_factorial > 1:
# #     factorial *= number_factorial
# #     number_factorial -= 1
# #
# # print(f'factorial equels: {factorial}')
# # check_login=input('enter login:')
# # while check_login == 'First':
# #     print(f'Hello! {check_login}')
# #     break
# # else:
# #     print('login error')
#
#
# # read_positiv_number=int(input())
# # while 0 !=read_positiv_number >0 :
# #     print(read_positiv_number)
# #     read_positiv_number = int(input())
# # else:
# #     pass
#
# # number_seqens= int(input())
# # number=tuple(input())
# # # if i in number <0:
# # #     pass
# # # else:
# # print(i if i in number <0 else '')
#
#
# # for number in range(10,31):
# #     if number%2==0:
# #         number_part=int(number/2)
# #         print(f'{number} equals {number_part}*2')
# #     else:
# #         print(f'{number} is prime number')
#
# # sentence='a sss ddddd fffffffff rr'
# # a=sentence.split()
# # print(i for i in a.sort())
# # input_str = input("Enter a string: ")
# #
# # # breakdown the string into a list of words
# # words = input_str.split()
# #
# # # sort the list
# # words.sort()
# #
# # print("The sorted words are:")
# # for word in words:
# #     print(word)
#
#
# # n = ['aaa', 'bbb', 'ccc', 'dddd', 'dddl', 'yyyyy']
# # sentence = str(input())
# # splited_sentence = sentence.split()
# # sorted_list=[words for words in (sorted(splited_sentence, key=len))]
# # sorted_sentence= (' '.join([str(word) for word in sorted_list]))
# # print (sorted_sentence)
#
#
# # def ser_ar(*args):
# #     if args!= ( ):
# #         return sum(args)/len(args)
#
# # def modulus(number):
# #     return number if number >0 else number * (-1)
# #
# # print (modulus(0))
# # def max_number(number1,number2):
# #     '''function returns max value of two numbers without equals exceptions'''
# #     return max(number1,number2)
# #
# # print(max_number(-5,-3))
#
# # def rectangle(side1,side2):
# #     return side1*side2
# # def triangle(bases, hight):
# #     return 1/2*bases * hight
# # def  circle(radius):
# #     return 3.14 * radius**2
# # def squere(rectangle,triangle,circle):
# #     return rectangle,triangle,circle
# #
# # print(squere(0,circle(3),0))
#
# # def sum_digits_numbers(number):
# #     return sum(int(digit) for digit in str(number))
# #
# # print(sum_digits_numbers(1340))
# # print(ser_ar())
#
#
# # def zero_fuel(distance_to_pump, mpg, fuel_left):
# #     while distance_to_pump == mpg*fuel_left or distance_to_pump < mpg*fuel_left:
# #         return True
# #         break
# #     else:
# #         return False
# # print(zero_fuel(50,25,2))
#
# # def enough(cap, on, wait):
# #     while cap >= on + wait: #or cap > (on +wait):
# #         return 0
# #     else :
# #         return ((on+wait)-cap)
# #
# #
# # print(enough(20,5,5))
# # print(enough(10,5,5))
# # print(enough(100,60,50))
#
# # def areYouPlayingBanjo(name):
# #     if name[0] == 'R' or name[0] == 'r':
# #         return f'{name} plays banjo'
# #     else:
# #         return f'{name} does not play banjo'
# #
# # print(areYouPlayingBanjo("rartin"))
#
# # def count_sheeps(sheep):
# #    return sheep.count(True)#sum(sheep)
# #
# # array1 = [True,  True,  True,  False,
# #           True,  True,  True,  True ,
# #           True,  False, True,  False,
# #           True,  False, False, True ,
# #           True,  True,  True,  True ,
# #           False, False, True,  True ];
# # print(count_sheeps(array1))
# # import pyowm
# #
# # owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key
# #
# # # Have a pro subscription? Then use:
# # # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# #
# # # Search for current weather in London (Great Britain)
# # observation = owm.weather_at_place('London,GB')
# # w = observation.get_weather()
# # print(w)                      # <Weather - reference time=2013-12-18 09:20,
# #                               # status=Clouds>
# #
# # #Weather details
# # #
# #
# # w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# # w.get_humidity()              # 87
# # w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# #
# # # Search current weather observations in the surroundings of
# # # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# # observation_list = owm.weather_around_coords(-22.57, -43.12)
#
# # import calculator
# # a= int(input('enter number:'))
# # b= int(input('enter number:'))
# # symbol = input('select an action:')
# # if symbol == '+':
# #     print(calculator.addition(a,b))
# # elif symbol == '-':
# #     print((calculator.substraction(a,b)))
# # elif symbol == '*':
# #     print(calculator.multiplication(a,b))
# # elif symbol == '/':
# #     print(calculator.division(a,b))
# #
# # import random
# #
# # client_number = int(input("Let's play,guess number:"))
# # computer_number = random.randint(0,100)
# # #print(computer_number)
# # while client_number!=computer_number:
# #     print ('your number is bigger,try once more'if client_number > computer_number else 'your number is smaller, try once more')
# #     client_number = int(input('say number:'))
# # else:
# #     print(f'you win, i ordered {computer_number}')
# # import math
# # def rectangle(side1,side2):
# #     return side1*side2
# # def triangle(bases, hight):
# #     return 1/2*bases * hight
# # def  circle(radius):
# #     return math.pi * math.pow(radius,2)
# # def square(rectangle,triangle,circle):
# #     return rectangle,triangle,circle
# #
# # print(square(0,circle(2),0))
#
#
# # import pyowm
# #
# # city=input("What city you are interested:")
# # owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key
# #
# # # Have a pro subscription? Then use:
# # # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# #
# # # Search for current weather in London (Great Britain)
# # observation = owm.weather_at_place(city)
# # w = observation.get_weather()
# # temperature=w.get_temperature('celsius')['temp']
# #
# # print("In " + city + " city" + " is the temperature of the air"+
# # " "+ str(temperature) + " for the Celsius")
# # print("In this city "+ w.get_detailed_status())
# #
# # #print(w)                     # <Weather - reference time=2013-12-18 09:20,
# #                               # status=Clouds>
# #
# # # Weather details
# # # w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# # # w.get_humidity()              # 87
# # # w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# # temperature=w.get_temperature('celsius')["temp"]
# # temperature_max=w.get_temperature('celsius')["temp_max"]# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# # print(f"Today temperature is {temperature}")
# #
# #
# # # Search current weather observations in the surroundings of
# # # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# # #observation_list = owm.weather_around_coords(-22.57, -43.12)
# #
# # def filter_words(st):
# #     splited=st.split()
# #     for i in splited:
# #         i=i.lower()
# #     print(i)
# #     #print(' '.join(st[:1].upper() + st[1:] for st in st.split(' ')))
# #
# # print(filter_words('hello WoW'))
# # class Car:
# #     def __init__(self,name,model):
# #         self.name=name
# #         self.model=model
# #     def start(self):
# #         print(f'{self.name}{self.model} start')
# #
# #     def stop(self):
# #         print(f'{self.name}{self.model} stop')
# #
# # if __name__=="__main__":
# #     a=Car('toyota','camry')
# #     a2=Car('bmw','m3')
# #     a2.start()
# #     a.start()
#
#
# # for i in range(0,22,4):
# #     for k in range(0,i):
# #         print(i-k)
# #         n=i+i
# #         for l in range(n,i):
# #             print([l])
# #     print([i] )
# # class InDef():
# #     def __init__(self,sticks,a,your_move):
# #         self.sticks=self
# #         self.a=a
# #         self.your_move=your_move
# #     #a=int()
# #         sticks = sticks - a
# #         print (f'my move:{a} stick{sticks}')
# #         your_move=int(input('you move:'))
# #         print((sticks-your_move) if your_move in range(1,4) else 'tttt')
# #         a=sticks-your_move
# # def make_move(sticks):
# #     sticks=int(input('sticks:'))
# #     a=int()
# #     if sticks==21:
# #         a=1
# #         in_def(sticks,a)
# #     elif 17<sticks<21:
# #         a=sticks-17
# #         in_def(sticks, a)
# #     elif 13<sticks<16:
# #         a=sticks-13
# #         in_def(sticks, a)
# #     elif 9<sticks<13:
# #         a=sticks-9
# #         in_def(sticks, a)
# #     elif 5<sticks<9:
# #         a=sticks-5
# #         in_def(sticks, a)
# #     elif 0<sticks<4:
# #         a=sticks-0
# #         in_def(sticks, a)
# #     else:a=0
# #     print(f'finish')
# #
# # print(make_move(21))
#
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         name=str()
# #         age=int()
# #     def info(self):
# #         print(self.name,'s age is ',self.age)
# #
# #
# # person=Person('o',9)
# #
# # # person.info()
# # def create_array(n):
# #     res=[]
# #     i=1
# #     while i<=n:
# #         res.append(i)
# #         i+=1
# #     return res
# #
# # print(create_array(3))
#
# # def count_positives_sum_negatives(arr):
# #     while arr!=[]:
# #         positive_arr=[i for i in arr if i>0]
# #         arnegative_arr=[k for k in arr if k<0]
# #         print([len(positive_arr),sum(arnegative_arr)])
# #         break
# #     else: print([])
#
# # count_positives_sum_negatives([])
# # def solution(number):
# #     return sum([i for i in range(1,number)if i%3==0 or i%5==0])
# #
# #
# # print(solution(10))
# # def reverse_list(l):
# #     l.reverse()
# #     return l
# # print(reverse_list([1,2,3,4]))
# # # def list_animals(animals):
# #     # animals=[f'{i}\n' for i in animals ]
# #     # list = []
# #     # for i in animals:
# #     #     list = f'{i}.{i} \n'
# #     #     i+=i
# #     #return ''.join ([f'{i}\n' for i in animals ])
# #     # return str(''.join ([f'{i}\n' for i in animals ]))
# # # return()
# #
# # def list_animals(animals):
# #     list = ' '.join(map(str, animals ))
# #     #list2=
# #     for i in list:
# #         return (f'{i}\n')
# ## def make_move(sticks):
# #     sub_marbles=0
# #     dr_nim=0
# #     sticks=list(range(1,sticks))
# #     while len(sticks) % 4 != 0 and sticks != 0:
# #         dr_nim = sticks.pop()
# #         sub_marbles += 1
# #         return sub_marbles
# #
# # animals = [ 'dog', 'cat', 'elephant' ]
# # print(list_animals(animals))
# # def double_char(s):
# #     return ''.join([i+i for i in s])
# #
# # print(double_char("Hello World"))
# # def is_uppercase(inp):
# #     return inp.isupper()
# # print(is_uppercase("="))
# # def capitalising_element(elem):
# #     return [a[0].capitalize() for a in elem]
# # def sorter(textbooks):
# #     r=[a[0].capitalize() for a in textbooks]
# #     return sorted(textbooks,key=capitalising_element())
# #     #return textbooks.sorted()
# #    # a =' '.join([i.capitalize() for i in textbooks])
# #     #return
# # print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']))
# #
# # # def filter_words(st):
# #   filtered_word_with_gap=(st[0].upper()+st[1:].lower())
# #   return ' '.join(filtered_word_with_gap.split())
# #   #filtered_word_with_gap.replace("  ","")
# # #
# # print(filter_words('UUYT     tt     TTT tytyr'))
#
#
# # names = ['Sam', 'Don', 'Daniel']
# # x=map(hash,names)
# # print(lambda i: hash,names)
# # #rint(list(x))
#
# # a=['1','2','3']
# #
# # x=map(int,a)
# # print(str(x))
# # print(type(x))
#
#
#
# # a=[1,2]
# # a.append([3,4])
# #
# # print(a[:])
# # a.extend((3,4))
# # print(type(a[2]))
# # print(a[:])
#
# # m=dict([(1,'a'),(2,'d')])
# # print(m)
#
#
# # def isPalindrome(str1):
# #     str1 = 'abb'
# #     #set1=set(str1)
# #     if len(str1)==len(set(str1))*2 -1:
# #         return True
# #     else :return False
# #     # pass
# # str1 = 'abb'
# # set1=set(str1)
# # print(isPalindrome(str1))
# # print(set1)
# # def findPermutation(n, p, q):
# #
# #     #r = [3, 2, 1]
# #     r=[i for i in range(n+1) if 1<=i<= n and q[i] == p[i]]
# #     return r
# # n = 3
# # p = [3, 1, 2]
# # q = [2, 1, 3]
# # #r = [3, 2, 1]
# # print(findPermutation(n,p,q))
#
# # def filterBible(scripture, book, chapter):
# #     return [i for i in scripture if book == i[0:2] and chapter == i[2:5]]
# # scripture = ["01222001",
# #              "01001002",
# #              "01002001",
# #              "01002002",
# #              "01002003",
# #              "02001001",
# #              "02001002",
# #              "02001003",
# #              "66022021"]
# # book = "01"
# # chapter = "222"
# # print(filterBible(scripture,
# #                   book,
# #                   chapter))
#
# # def toPostFixExpression(e):
# #     r=["+","-","/","*"]
# #     list_out=[i for i in e if i not in r and i!="(" and i!=")"]
# #     list_in=[i for i in e if i in r]
# #
# #     return list_out+list_in
# # e=["20","+","3","*","(","5","*","4",")"]
# #
# # print(toPostFixExpression(e))
#
#
# # def order(a):
# #
# #     if sorted(a)==a:
# #         return "ascending"
# #     elif sorted(a,reverse=1)==a:
# #         return "descending"
# #     else: return 'not sorted'
# #
# # a = [10,6,5]
# # print(sorted(a,reverse=1))
# # print(sorted(a))
# # #order(a) = "descending"
# # print(order(a))
# # def Cipher_Zeroes(N):
# #     l=[0,6,9]
# #     n=[int(x) for x in str(N)]
# #     point_1=len([i for i in n if i in l])
# #     print(point_1)
# #     point_2 = len([i for i in n if i == 8])*2
# #     sumOfPoint=point_1+point_2
# #     if sumOfPoint%2==0 and sumOfPoint>0:
# #         return f"{(sumOfPoint+1):b}"
# #     elif sumOfPoint<=0:
# #         return 0
# #     else :return f"{(sumOfPoint-1):b}"
#
#
# # N=565
# # # print(Cipher_Zeroes(N))
# # # #print(f"{(5):b}")
# # # print(5/2)
#
# #def kthTerm(n, k):
#   # #  For  #   n = 3 and k = 4, the  #   output  #   should  #   be  #   kthTerm(n, k) = 9.
#   #
#   #   For
#   #   n = 3, the
#   #   sequence
#   #   described
#   #   above
#   #   begins as follows: 1, 3, 4, 9, 10, 12, 13...
#   #   [3 ** 0] = > [1]
#   #   [1, 3 ** 1, 3 ** 1 + 1] = > [1, 3, 4]
#   #   [1, 3, 4, 3 ** 2, 3 ** 2 + 1, 3 ** 2 + 3, 3 ** 2 + 4] = > [1, 3, 4, 9, 10, 12, 13]
#   #   ...
#   #
#   #   The
#   #   4
#   #   th
#   #   number in this
#   #   sequence is 9, which is the
#   #   answer.
# #   g=n**0
# #   p=1
# #   y=[g,n**g,n**g+p]
# #   while len(y)<=k:
# #     for i in y:
# #           p = y[i]
# #       #     for i in y:
# #       #         g=i
# #           y.extend(y)
# #
# #
# #   return y
# #
# #     #return [i for i in n**k if 2 <= n <= 30 and 1 <= k <= 100]
# #
# # print(kthTerm(3,4))
# #
# # 1]
# # 3**1 = 3
# # [1,3, 3+1]
# # 3**2=9
# # [1,3, 4, 9, 9+1,9+3, 9+4]
# # 3**3=27
# # [1,3, 4, 9, 10,12, 13, 27, 27+1, 27+3, 27+4, 27+9, 27+10, 27+12,27+13]
#
# # f='qwerty'
# # # index=0
# # # while index<len(f):
# # #     letter=f[index]
# # #     print(index,letter)
# # #     index=index+1
# # r='qwerty ttt'
# # print('123'.center(6,'o'))
# # print(r.count('t',1))
# # print(r.expandtabs())
# # print(r.find('t',5,8))#return index from slice
# # print('yyy {}'.format(r),f'yyy {r}',)
# # print('{0}{1}{0}'.format('abra', 'cad'),)
# # print('{2}, {1}, {0}'.format(*'abc'))
# # print("Units destroyed: {players[0]}".format(players = [1, 2, 3]))#choose from list by index
# # print('r'.isalnum())#return false if not num or letter
# # print(r.join('Uop'))
# # print(r.replace('ttt','ooo'))
# # print(' YYYu'.strip())
#
#
#
# # def double_string(data):
# #     u = [set(i) for i in data]
# #     # print(u)
# #     # print(set([str(i) for i in u]))
# #     p=set([str(i) for i in u])
# #     # if len(u)!=len(p):
# #     #     return len(p)
# #     # else: return 0
# #     return len(p) if len(u)!=len(p) else 0
# #
# # data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
# # #data = ['aa', 'abc', 'qwerqwer']
# # print(double_string(data))
# # import re
# #
# # def figure_perimetr():
# #     distance1=(x1, y1, x2, y2)
# #
# #     LB=
# #     return round(((x1-x2)**2 + (y1-y2)**2)**0.5,2)
# # import re
# # #self = "#LB1:1#RB4:1#LT1:3#RT4:3"
# # def figure_perimetr(self):
# # #self = "#LB1:1#RB4:1#LT1:3#RT4:3"
# # #pattern = re.compile(test1)
# #     points = re.findall(r'\d[:]\d',self)
# #     LB,RB,LT,RT,= points
# #
# #     x1,y1=[int(i) for i in re.findall(r'\d',LB)]
# #     x2,y2=[int(i) for i in re.findall(r'\d',RB)]
# #     LB_RBside=((x1-x2)**2 + (y1-y2)**2)**0.5
# #     # print(x1,y1,x2,y2)
# #     # print(LB_RBside)
# #     x1,y1=[int(i) for i in re.findall(r'\d',RB)]
# #     x2,y2=[int(i) for i in re.findall(r'\d',RT)]
# #     RB_LTside=((x1-x2)**2 + (y1-y2)**2)**0.5
# #     # print(x1,y1,x2,y2)
# #     # print(RB_LTside)
# #     x1,y1=[int(i) for i in re.findall(r'\d',RT)]
# #     x2,y2=[int(i) for i in re.findall(r'\d',LT)]
# #     RT_LTside=((x1-x2)**2 + (y1-y2)**2)**0.5
# #     # print(x1,y1,x2,y2)
# #     # print(RT_LTside)
# #     x1,y1=[int(i) for i in re.findall(r'\d',LT)]
# #     x2,y2=[int(i) for i in re.findall(r'\d',LB)]
# #     LT_LBside=((x1-x2)**2 + (y1-y2)**2)**0.5
# #     # print(x1,y1,x2,y2)
# #     # print(LT_LBside)
# #     print(LB_RBside+RB_LTside+RT_LTside+LT_LBside)
# #     #print(x1,x2,x3,x4,x5,x6,x)
# #     print(LB,RB,LT,RT)
# #
# #     # for p in points:
# #     #     p = re.split(r'L',points)
# #     # print(p)
# #     #for i in points:
# #     print(points)
# #     # def figure_perimetr(a):
# #     #     patern=re.compile(r'\w\w\d[:]\d')
# #     #     print(patern)
# #     #     Lb=patern.search('LB')
# #     #     print(Lb)
# #     #     return Lb
# # test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# # print(figure_perimetr(test1))
#
# # import re
# # def pretty_message(self):
# #     #\b\w{3}\b
# #     self = "Thisssss"
# #     # last3 = re.findall(r'\w{3}\b',self)#end of word
# #     # last= re.findall('(last3)\b',self)
# #     # print(last3,last )
# #     #a=re.sub(r'(\w{1,})\b','', self)
# #     a=re.split(r'\w{3}\b',self)
# #     #a = re.findall(r'\w*\S\b', self)
# #     print(a)
# #     #y = [sorted(set(i), key=lambda d: i.index(d)) for i in a]# Впорядкована множина
# # #     print(y)
# # #     t = ' '.join([''.join(i) for i in y])
# # #     return(t)
# # #     #return [set(i) for i in self ]
# # data = "Thisssssssss "
# # print(pretty_message(data))
# # # n=[]
# # a = re.findall(r'\w*\S\b', data)
# # y =[sorted(set(i), key=lambda d: data.index(d)) for i in a]
# # print(a,y)
# # list=[['T', 'h', 'i', 's'], ['i', 's']]
# # t=' '.join([''.join(i) for i in list])
# # print(t)
#
#
# # import re
# # def max_population(data):
# #
# #
# #     data = ["id,name,poppulation,is_capital","3024,eu_kyiv,24834,y","3025,eu_volynia,20231,n",
# # "3026,eu_galych,23745,n",
# # "4892,me_medina,18038,n",
# # "4401,af_cairo,18946,y",
# # "4700,me_tabriz,13421,n",
# # "4899,me_bagdad,22723,y",
# # "6600,af_zulu,09720,n"]
# #     ss=(str(data))
# #     pattern = re.compile(r'\d\d\d\d[,]\w*[,]\d*[,]\w')
# #     # for pattern in data:
# #     #     return pattern
# #     qqq=dict((re.findall(r'\d\d\d\d[,](\w*)[,](\d*)[,]\w', ss)))
# #     #return dict((re.findall(r'\d\d\d\d[,](\w*)[,](\d*)[,]\w',ss)))
# #     return max(qqq, key=qqq.get), max(qqq.values())
# #
# #     # for m in result:
# #     #     print(m)
# #
# # def f6(arg):
# #     arg+=5
# #     return arg
# #
# #
# # x=(1)
# # f6(x)
# # print(x)
# # print(f6(x))#############чомму передає 5????????????
#
# # def func1(x):
# #     def func2(y):
# #         return x*y
# #     return func2
# #
# # res=func1(10)
# # print(res(5))
#
# # def f1():
# #     s='outer'
# #     def f2():
# #         nonlocal s
# #         s+='inner'
# #         print(s)
# #     return f2
# # res=f1()
# #print(res())
#
# # def power_generator(num):
# #     def power_n(power):
# #         return num**power
# #     return power_n
# #
# # p2=power_generator(2)#передаємо num
# # p3=power_generator(3)
# # print(p2(8))#передаємо power
# # print(p3(4))
#
# # def decorator(func):#############DECORATOR
# #     def wrap():
# #         print('decoration')
# #         func()
# #         print('again print')
# #     return wrap
# #
# # @decorator
# # def h_w():
# #     print('Hello world')
# #
# # h_w()
#
# # def coundown(num):
# #     print('start')
# #     while num > 0:
# #         yield num
# #         num-=1
# #
# # val = coundown(4)
# # print(iter(val))
# # print(next(val))
# # def o (a,b):
# #     def i(c,d):
# #         return c+d
# #     return i(a,b)
# #     return a
# #
# # r=o(7,10)
# # print(r)
# # def f(a):
# #     a=[3,4]
# #     print(a, end=" ")
# # a=[1,2]
# # f(a)
# # print(a)
# # def o():
# #     m="o"
# #     def i():
# #         global m
# #         m="i"
# #     i()
# #     return m
# # print(o())
# # def o(x):
# #     return lambda : x**2
# # print(o(5))
#
# # def f(i,l=[]):
# #     l.append(i)
# #     print(l, end='')
# #
# # f(1)
# # f(2)
# # def ad(a):
# #     a.append(3)
# #
# # b=[1,2]
# # ad(b)
# # print(b)
# # def f(i,s=5):
# #     s+=i
# #     print(s, end=' ')
# # f(1)
# # f(3)
# # def outer(name):
# #     def inner():
# #         print (f'Hello {name}!')
# #     return inner
# #
# #
# # tom=outer("tom")
# # tom()
#
# # def create(a):
# #     def anonym(b):
# #         return True if a == b else False
# #     return anonym
#
# # create=lambda a:lambda c:c==a
# #      #return True if b==a else False
# # print(create("pass_for_Tom"))
# # #print(list(get_names(create)))
# # tom = create("pass_for_Tom")
# #
# # print(tom("pass_for_Tom"))#returns true
#
# # import re
# # password = 'qQ1345'
# # pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=_*]).*$"
# # pass_chek = re.findall(pattern, password)
# # if pass_chek:
# #     print(True)
# # else:raise ValueError
#
# # secret_words=["word1", "abc3", "list"]
# # secret_words_1=["word1", "z"]
# # # f=[i for i in secret_words if i in secret_words_1]
# # # g=[i for i in secret_words if i not in secret_words_1]
# # l=[]
# # l2=[]
# # for i in secret_words_1:
# #     l2.append(i)#(','.join(secret_words_1))
# # #print(l2)
# # for i in secret_words:
# #     if i in l2:
# #         l.append(i)
# #         l2.remove(i)
# #     else: pass
# # print(l,l2)
# # print(len(l2))
# # if len(l2)<=1:
# #     print(True)
# # else:print(False)
# #print(f,g)
# # print(len(f)-len(g) or len(f)-len(g)>1)
# #print(len(secret_words))
# #if len(f)-1 == len(secret_words) or len(secret_words) == len(f)+1:
# # if len(f)-len(g)<=1 or len(f)==len(g):
# #     print(True)
# # else: print(False)
#
# # t = (''.join(secret_words))
# # t1 = (''.join(secret_words_1))
# # print(t,t1)
# # sw_chek=re.findall(t,t1)
# # print(sw_chek)
#
# # def create_account(user_name, password, secret_words):
# #     def chek(password_1, secret_words_1):
# #         # secret_words22=str(secret_words)
# #         # secret_words_11=str(secret_words_1)
# #         # print(password, secret_words22)
# #         # print(password_1,secret_words_11)
# #         pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=_*]).*$"
# #         pass_chek = re.findall(pattern, password)
# #         if pass_chek:
# #             t = sorted(''.join(secret_words))
# #             t1 = sorted(''.join(secret_words_1))
# #             print(t1)
# #             y = set(t + t1)
# #             return( True if password==password_1\
# #                            and len(y)-len(t1)<=1\
# #                            and len(y)-len(t)<=1 \
# #                     else False)
# #
# #         else: raise ValueError
# #     return  chek
# # import re
# # def create_account(user_name, password, secret_words):
# #     pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!?@#$%^&+=_*]).*$"
# #     pass_chek = re.findall(pattern, password)
# #     if not pass_chek:
# #         raise ValueError
# #     else:
# #         def check(password_1, secret_words_1):
# #                     l = []
# #                     l2 = []
# #                     for i in secret_words_1:
# #                         l2.append(i)
# #                     for i in secret_words:
# #                         if i in l2:
# #                             l.append(i)
# #                             l2.remove(i)
# #                             #print(l,l2)
# #                     return  password == password_1\
# #                            and ((len(l) - len(l2)) >= 1 or len(l)==len(l2))\
# #                            and len(secret_words)==len((secret_words_1))
# #         return check
# # # tom = create_account("Tom", "Qwerty", ["1", "word"])
# # # print(tom("Qwerty1!",  ["word", "12"]))
# # # val1 = create_account("123", "qQ1!45",[1,1,1])
# # # val1("qQ1!45", [2,1,1])
# #
# # tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# # print(tom("Qwerty1_",  ["1", "word"]))
#
# # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
# # print(user2("yu6r*Tt5",["abc3", "word1", "list"]))
#
# # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
# # print(user2("yu6r*Tt5",["abc3", "abc3", "abc3"]))
#
# # secret_words =["word"]
# # secret_words_1 = ["wor"]
# # t=sorted(''.join(secret_words))
# # t1=sorted(''.join(secret_words_1))
# # print(t,t1)
# # y=set(t+t1)
# # print(y)
# # if len(y)-len(t1)<=1 and len(y)-len(t)<=1:
# #  print('ok')
# # else: print("xxxxxx")
#
# def divisor(n):
#
#         for i in range(1, n):
#             if n % i == 0:
#                 yield i
#
#         yield n
#         while True:yield None
#
#
#
# three = divisor(3)
# print(next(three))
# print(next(three))
# print(next(three))
# print(next(three))


# def logger(fn):
# #     def wrapper(*arg,**kwarg):
# #         print("Executing of function " + str(fn.__name__) + " with arguments " + str(arg))
# #         fn(*arg,**kwarg)
# #
# #     return wrapper
# #
# #
# # @logger
# # def concat(*arg,**kwarg):
# #     print(f'{arg,kwarg}')
# #     return (f'{arg,kwarg}')
# #
# #
# # @logger
# # def sum(a, b):
# #     return a + b
# #
# #
# # @logger
# # def print_arg(arg):
# #     print(arg)
# #
# # #print(concat('first string', second = 2, third = 'second string'))
# # print(sum(2,3))

# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for a in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
#
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
#
# a=Polygon(3)
# a.inputSides()
# a.dispSides()


# class Par1 (object):
#     def method_1(self):
#         return '(Par1 method_3)'
#     def method_2(self):
#         return '(Par1 method_2)'
#
# class Par2 (object):
#     def method_2(self):
#         return '(Par2 method_2)'
#     def method_3(self):
#         return '(Par2 method_3)'
# class Child (Par1, Par2):
#     pass
# x = Child()
# print (x.method_1(), x.method_2(), x.method_3())
#
# #(Par1 method_3) (Par1 method_2) (Par2 method_3)
# class Child (Par2, Par1):
#     pass
# x = Child()
# print (x.method_1(), x.method_2(), x.method_3())
#
# (Par1 method_3) (Par2 method_2) (Par2 method_3)

# class Animal:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name
#     def talk(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Cat(Animal):
#     def talk(self):
#         return 'Meow!'
#
# class Dog(Animal):
#     def talk(self):
#         return 'Woof! Woof!'
#
# animals = [Cat('Missy'),
#            Cat('Mr. Mistoffelees'),
#            Dog('Lassie')]
#
# for animal in animals:
#     print (animal.name + ': ' + animal.talk())
# class s:
#     def __init__(self,id=0):
#         self.id = id
#         #id = 100
# class S(s):
#
#     def __init__(self,id2=0):
#         s.__init__()
#         self.id2 = id2
#
# def main():
#     b=S()
#     b.id=2
#     b.id2=9
#     print(b.id)
#     print(b.id2)

# main()

# val = s(100)
# val.__dict__['age'] = 49
#
# print((val.__dict__))

# class A:
#     def __init__(self):
#         self.calcI(30)
#        # print(' i from A is',self.i)
#
#     def calcI(self,i):
#         self.i = 2 * i;
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print(' i from B is', self.i)
#
#     def calcI(self,i):
#         self.i = 3*i;
#
# b = B()
# #A.isinstance(b)
# isinstance(b, A)
# #isinstance(A, b)
# #b.isinstance(A)

# class Employee():
#     def __init__(self, firstname, lastname, salary):
#         self.firstname = firstname;
#         self.lastname = lastname;
#         self.salary = salary;
#         #print(firstname, lastname, salary)
#
#     @classmethod
#     def from_string(cls,x):################################classmethod наслідує ініт від емплої
#         cls.firstname, cls.lastname, cls.salary =list(x.split("-"))
#         return cls
# #emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# print(emp2)
# #print(emp1.firstname)# ➞ "Mary"
# # emp1.salary #➞ 60000
# print(emp2.firstname) #➞ "John"

# class Pizza:
#     _counter = 0
#     def __init__(self,ingredients, order_number = 0):
#         self.ingredients =  ingredients
#         Pizza._counter += 1
#         self.order_number = Pizza._counter;
#
#     def __repr__(self):
#         return f'{self.ingredients}'
#
#     # @classmethod
#     # def from_list(cls,x):
#     #     cls.ingredients = input("Enter ingrients "+str(i+1)+" : ")
#     #     print(cls.ingredients)
#     #     return cls
#
#     @classmethod
#     def hawaiian(cls):
#         return cls(['ham', 'pineapple'])
#
#     @classmethod
#     def meat_festival(cls):
#         return cls(['beef', 'meatball', 'bacon'])
#
#     @classmethod
#     def garden_feast(cls):
#         return cls(['spinach', 'olives', 'mushroom'])
#
# p2 = Pizza.garden_feast()
# p1 = Pizza(["bacon", "parmesan", "ham"])
# print(p2)

# class Obj:
#     _counter = 0
#     def __init__(self,ooo):
#         self.ooo = ooo
#         Obj._counter += 1
#         self.id = Obj._counter
#
#
# r = Obj(2)
# r1 = Obj(3)
# r2 = Obj(3)
# print(r2.id)

# class Employee:
#     def __init__(self,x,**properties):
#         self.name, self.lastname,  = list(x.split(" "))
#         for key, value in properties.items():
#              setattr(self, key, value)
# import json
# import re

# def find(file, key):
# with open('1.json', 'r') as file:
#     d_dict = json.load(file)

# for d in d_dict:
# key = "password"
#     # s =file.items() # set(file.items())
#     # return s#(p)
# d_dict = [{"name": "user_1", "credentials": {"username": "user_user", "password" :"1234qweQWE"}}, {"name": "user_2", "password": ["pass_1 ", "qwerty "]}]


# # print(list(fun(d)))# "password"))# returns ["1234qweQWE", "pass_1", "qwerty"]
# m_dict = [dict(i) for i in d_dict]
# dic = {}
# di = [dict(i).values() for i in d_dict if isinstance(i, dict)]
# print(di.)
# for i in di:
#     if isinstance(i,dict):
#         print(i)
# h = [dict(k).values() for k in di ]
# di.get("bogus", None)
# print(h)
# print(type(m_dict))
# d =[dict(i).get(key) for i in m_dict if dict(i).get(key)!=None ] #if dict(i).keys() == key] # for i in d_dict]
# d = d_dict.sort(key,)
# print(d)
# print( [i for i in d if i not in i])


# find("1.json", "password")# returns ["pass_1", "qwerty"]
# print(set(d_dict.values()))#[i for i in d_dict])
# str([i for i in d_dict if key == i])])
# print(find(d_dict, 'password'))

# 1.json:
# [{"name": "user_1”, "password": "pass_1”},
# {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
# print(find("1.json", "password") #returns ["pass_1", "qwerty"])
# from __future__ import print_function
# import json

# def find(file,key):
#     results = []
#
#     def _decode_dict(a_dict):
#         try:
#             while type(file) == str:
#                 results.extend(a_dict[key])
#                 break
#             else: results.extend([a_dict[key] for i in file])
#         except KeyError:
#             pass
#         return set(a_dict)
#
#     json.loads(file, object_hook=_decode_dict) # Return value ignored.
#     return results
#
# file = {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
# print(find(file, "password"))# returns ["1234qweQWE"]
# file = '{"name": "user_1", "password": "pass_1", "name": "user_2" , "password": ["pass_1", "qwerty" ]}'
# print(find(file,'password'))

# def fun(d):
#     if 'password' in d:
#         yield d['password']
#         print(d['password'])
#     for k in d:
#         if isinstance(d[k], dict):
#             print(d[k])
#             # for i in d[k]:
#             #     for j in fun(i):
#             #         yield j
#             #         print(j)
#
# d = [{"name": "user_1", "credentials": {"username": "user_user", "password" :"1234qweQWE"}}, {"name": "user_2", "password": ["pass_1 ", "qwerty "]}]
# print(list(fun(d)))# "password"))# returns ["1234qweQWE", "pass_1", "qwerty"]
# import unittest
# def divide(a,b):
#     if b!=0:
#         return  a/b
#     raise Exception("Division by zero")

# def f(a):
#
#     a=[3,4]
#     print(a, end = " ")
#
# a = [1,2]
# f(a)


# def many(arg, *args, **kwargs):
# #     print(args, kwargs)
# #
# # many(1,2,3, b=4,name = 'first name', job='ff')
# print((test_sum()))
# def func(item,stuff=5):
#     stuff+=item
#     print(stuff,end =" ")
#
#
# func(1)
# func(3)
#
# list = ["item1", 1, "item3"] # line 1
#
# with list as a:                   # line 2
#
#     print(a)                        # line 3

# def f(i,l=[]):
#     l.append(i)
#     print(l,end=' ')
#
# f(1)
# f(2)
# def add_v(a):
#     a.append(1)
#
# b=[1,2]
# add_v(b)
# print(b)
# t='123456789'
# print(t[:4]+' '+ t[:-4]+' '+ t[-4:])
# print([(i**2) for i in range(20) if i>3])
# print([(i**2)%10 for i in range(20) if i>3])
# print([(i**2)//10 for i in range(20) if i>3])
# print([(i**2)//10 for i in range(20) if i>3 and ((i**2)//10/2)%1!=0])


# sheeps = int(input("enter number of the sheeps:"))
# magic6 = [(i**2)%10 for i in range(sheeps) if i>3 and ((i**2)//10/2)%1!=0]
# try:
#     while (i==i+1 for i in magic6 ):
#         print(f'knife_prise = ',(10+magic6[0])/2-magic6[0],'грн.')
#         break
# # except IndexError:
# #     print("Немає що ділити)....замало, для умови задачі")
# # #print([(i**2)%10 for i in range(sheeps) if i>3 and ((i**2)//10/2)%1!=0])
# # print([((i**2)//10/2)%1 for i in range(20) if i>3])
#
# a=[1,2,2]+[22]+[True]*int(2/1)+[ i for i in range(10) ]
#
# a.append({'q':45,"y":24})
# print(a)
# a.extend({'w':1})
# print(a)
# a.insert(0,"index place - insert")
# print((a))
#
#
# k=a.pop()#видаляє останній елем.
# print(a,'\n',k)
# a.pop(0)# del. elem. by index
# print((a))
# a.remove(2)#del.elev.by value - first in order
# print(a)
#
# a.reverse()
# print(a)
#
# a.sort()
# print(a)
#
# iter()
# a=1
# b=2
# c=3
# d=4
# b = [[('lk',0),23],[23,333]]
# a=dict(b)
# print([(type(k),type(v)) for k,v in a.items()])
# d = dict(a=1, b=2, f=3)
# print(d.clear())
# print(type(d))

# double_dict1 ={{v*2} for (v) in d.values() if v in range(10)}
# print (type(double_dict1))
# print (next(iter(double_dict1)))
# print (next(double_dict1))
# # print (next(double_dict1))
# d1 = {}
# print(d.values())
# print(d1)
# print(d)
# print(id(d['b']))
# print(id(b))
# a=1
# print(id(a))
#
# print((d))
# print(str([i for i in '123']).join({'a':2,'d':3}))
# r={'ss':2,'ff':3,'aaa':3}.
# print([i for i in sorted(r.items(),key=lambda para: (para[1],para[0]))]) ### sorted dict ! by value (para[1] and then key
#
# print('aaaa\\ssss')
# print('aaa\'sss')
# print('aaa\"sss')
# print('aaa\asss')
# print('aaa\bsss')
# print('aaa\fsss')
# print("aaa\nsss")
# print('aaa\tsss')
# print('aaa\vsss')

# a = list({1: 11, 2: 22, 3: 33}.values())
# b={1: 11, 2: 22, 3: 33}
# b=('1','2','3')
# #x=(lambda z,c: z+[list(c.keys())])
# x=tuple(map(lambda f:(f),b))
# print(x)
# #print (b.values())
# print (a)
# # d=(i for i in a)
# g= (i for i in a)
# print (d)
# print(id(d),id(g))
# print(next(d),id(next(d)))
# print(next(d),next(g),id(next(g)))
# print(a)
# b=2
# def x(b):
#     b=1
#     return b
# b=(lambda d:d)
# print(x(b))
# print (b(9))
# a,b,*c,f=(1,2.3,4,5,3,55)
# print (a,b,c[0],f)
# def f(a,b,c,d):
#     print(a,b,c,d)
#
# x=(1,2,3,4)
# f(*x)

# def f(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s,i
# print (f(1,2,3,4,5,6,7))
# a=3
# print(a==a)
# def rec(x):
#     if x<3:
#      rec(x+1)
#      print(x)
#
# rec(1)
# for _ in range(10):
#     print('rrr')
# a=(10,20,30,'q')
# #print(list(enumerate(a)))
# for i,y in enumerate(a,1):
#     print(i,y)
# a = [i*y+t for i in [1,2,3] for y in 'asd' for t in ('A')]
#
# print(a)
# def gen():
#     for i in range(5):
#         yield i
# s=gen()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
#
# def f(x):
#     return len(x)
#
# a=['q','qqq','qqqqq']
# b=list(map(f,a))
# d=list(map(lambda x:x+'!',a))
# print(d)
#
# s = list(map(int,input().split()))
# print(s)
# a=[1,2,3,4,6,5]
# b={100,100,20,40}
# c='asdf aaa'
# #a.sort()-new a
# #a=a.sort() - error
# #a=sorted(a) - new a - list type
# #print(sorted(a),sorted(b),sorted(c))
# #print(c.split(' '))- with str only
# print('#'.join(c))
#
# print(list(zip(a,b,c)),type(b))
# rez=zip(a,b,c)
# colection1,colection2,colection3=zip(*rez)
# print(colection1,colection2,colection3)
name = 'Andrii'
money = 100000
text = "Dear {0} you win {1} dollars".format(name, money)
text2 = f"Dear {name} you win {money} dollars"
text3 = "Dear {name} you win {money} dollars".format(name=name, money=money)
print (text, text2,text3, sep='  ')
print (text2)
