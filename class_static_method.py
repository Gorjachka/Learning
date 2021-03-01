# https://www.youtube.com/watch?v=rZY9CJn1y2E&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=13
class vector:
    min_coord = 0
    max_coord = 100

    def setCoords(self, x, y): # звичайний медот, що потребує екземпляру
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):# метод , що працює без екземпляру над атрибутами класу(min_coord,max_coord)

        if arg >= cls.min_coord and arg <= cls.max_coord:
            return True
        return False

    @staticmethod
    def norm2(x, y):# метод що не працює з елементами класу - сам по собі
        return x ** x + y ** y

print(vector.validate(2))
v=vector
v.x=1
v.y =10
print(v.x,v.y)
print(v)
print(vector.max_coord)
print(vector.norm2(2,3))