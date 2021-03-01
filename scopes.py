y='yellow'
def colors():
    #global y
    y='yellow local'


    def red():
        global y
        #nonlocal y
        y=2
        #y='yellow local_2'

        print('red',y)

    def blue():
        print ('blue')

    print (y)
    red()
    print (y)

    #blue()
colors()
print (y)