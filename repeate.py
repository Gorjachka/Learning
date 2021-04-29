# def logger(fn):
#     def wrapper(*arg, **kwarg):
#         print("Executing of function " + str(fn.__name__) + " with arguments " + str(arg))
#         fn(*arg, **kwarg)
#
#
#     return wrapper
#
#
# @logger
# def concat(*arg, **kwarg):
#     print(f'{arg, kwarg}')
#     return (f'{arg, kwarg}')
#
#
# @logger
# def summa(a, b):
#     return a + b
#
#
# print(concat('first string', second = 2, third = 'second string'))
# print(summa(2,3))
a={1,1,2,3,3}
f=(88,3)
v=a.issubset(f)
print(a,v)