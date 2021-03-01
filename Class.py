#https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3
class Car():
    wheel = 4 # дані для загального класу
    seets = 4
    # __ShsredAttribyte = {
    #     "whell":4
    #     "seets":4
    # }
    # def __init__(self):
    #     self.__dict__=Car.__ShsredAttribyte -- патерн моностану, тобто зміна атрибуту у всіх екземплярах

    #__slots__ = ['__wheel', '__seets'] метод для фіксації атрибутів, тобто тільки ці атрибути можемо використовувати
    def __init__(self,wheel, seets): #конструктор - присвоює екземпляру
        self.__wheel = wheel
        self.__seets = seets

    def __checkValue(x):# прихований метож класу, що не відноситьсядо екземрляру, що перевіряє данід
        if isinstance(x,int):
            return True
        return False
    def setOptions(self,wheel,seets): #сеттер, згідно цього методу можемо міняти захищенні атрибути
        if Car.__checkValue(wheel) and Car.__checkValue(seets):
            self.__wheel = wheel
            self.__seets = seets
        else: print('Value shoud be int')

    def getOptions(self,wheel,seets):# геттер отримуємо засетенні дані або дані чарівного методу
        return self.__wheel, self.__seets


    def drive(self, speed):#селф присвовує дані екземпляру в методі
        self.speed = speed
        print(self.__dict__)

    #def __del__(self):# деструктор, видаляє екземпляри класу
     #   print('видалення екземпляру'+self.__str__())

    # def __setOptions(self,wheel): #прихований сеттер, (викликається з проперті) згідно цього методу можемо міняти захищенні атрибути
    #     if Car.__checkValue(wheel): #and Car.__checkValue(seets):
    #         self.__wheel = wheel
    #        # self.__seets = seets
    #         print(f'seeter:{wheel}')
    #     else: print('Value shoud be int')
    #
    # def __getOptions(self):#прихований геттер (викликається з проперті) отримуємо засетенні дані або дані чарівного методу
    #     return self.__wheel

    #options = property(__getOptions,__setOptions)

    # def __repr__(self,wheel,seets): #вказує розробнику що за обєкт
    #     return f' object Car{self.wheel,self.seets}'
    #
    # def __str__(self,wheel,seets): # описуємо сам об.кт
    #     return  f'Car{self.wheel,self.seets}'

roadster = Car(4,2)# сторюємо екземпляр класу КАр з атрибутами колеса і місця
#roadster.manual_speed=5# присвоєння екземрляру атрибуту поза класом
#roadster.drive(22)
#roadster.options = 11 #записуємо за допомогою проперті в сетер
#x = roadster.options # читаємо з гетера
#print(x) #виводиимо
#roadster.setOptions(22,1)# перезаписуїмо атрибути екземпляру
#print(roadster.getOptions(22,1))# отримуємо, бачимо нові атрибути
#print(roadster.wheel)
