# def decorator(func):
#
#     def inner(*args,**kwargs):
#         print ('start decorator...')
#         func(*args,**kwargs)
#         print('end decorator...')
#
#     return inner
#
# @decorator #замість say = decorator(say)
# def say(name,surname):
#     print ('Hello',name,surname)
#
# say('Andrii','Gor')

from functools import wraps  # варінт декорування для збереження імені і документації


def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print ('<h1>')

    # inner.__name__=func.__name__ #щоб не пропадало імя на inner
    # inner.__doc__ = func.__doc__
    return inner


# @header
# def text_on(text1, text2):
#     print('texts are:', text1, text2)

@header
def sqr(x):
    '''
    Функціф підносить до квадрату
    :param x:
    :return:
    '''
    print (x ** 2)


# text_on('qqq', 'www')
sqr(3)
print (sqr.__name__,sqr.__doc__)
