# def main_func(value):
#     #name = value
#
#     def inner_func():
#         print('hello',value)#name)
#
#     return inner_func
#
# d=main_func("Andy")
# d()
# v=main_func('Dima')
# v(),d()


def counter():
    count = 0

    def inner():
        nonlocal count
        count +=1
        return count

    return inner


f = counter()
f()
f()
