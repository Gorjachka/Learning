from tkinter import *

root = Tk()

root.title('Page')

# елементи сторінки
enter_field = Entry(width=20)
button_field = Button(text="Transform")
label_field = Label(bg='yellow', fg='black', width=20)


def strToSortlist(event):
    set_field = enter_field.get()
    set_field = set_field.split()
    set_field.sort()
    label_field['text'] = ' '.join(set_field)


button_field.bind('<Button-1>', strToSortlist)

# розміщаємо елементи один за одним
# pack пакувальник, який дозволяє розміщати
# зображення одне за одним
# fill=BOTH дозволяє заповнювати все доступне місце і по ширині і по висоті
# expand=1 при розширенні вікна мітка завжди буде посередині

enter_field.pack()
button_field.pack()
label_field.pack()

# головний цикл

root.mainloop()