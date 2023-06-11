from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.json')
    data = text.get('1.0', END)
    try :
        out.write(data.rsplit())
    except Exception:
        messagebox.showerror("Ошибка!")

def open_file():
    global file_name
    inp = askopenfile(more='r')
    if inp is None:
        return
    file_name = inp.name
    data = inp.read()
    text.delete('1.0',END)
    text.insert('1.0',data)    
    


window = Tk()
window.title("Заметки")
window.geometry("400x400")
text = Text(window, width=400, height=400)
text.pack()



#window.option_add("*tearOff", FALSE)

main_menu = Menu(window)
file_menu = Menu(main_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Save",command=save_as)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_separator()


main_menu.add_cascade(label="File", menu=file_menu)




window.config(menu=main_menu)
window.mainloop()
