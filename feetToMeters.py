from tkinter import *

root = Tk()
root.title("Feet to Meters")
root.geometry("250x100") 

photo = PhotoImage(file = "ruler.png")
root.iconphoto(False, photo)

def Calculate(*arg):
    try:
        value = float(foot.get())
        result = int(0.3048 * value * 10000 + 0.5)/ 10000
        meters.set(result)
    except ValueError:
        meters.set("ERROR")

def quit():
    root.quit()

frame = Frame(root, padx=12, pady=4)
frame.grid(column=0, row=0)
frame.pack(padx=10, pady=10)

foot = StringVar()
foot_input = Entry(frame, width=7, textvariable=foot)
foot_input.grid(column=1, row=0)

meters = StringVar()
meters.set("0")
Label(frame, textvariable=meters).grid(column=1, row=1)

Button(frame, text="Calculate", command=Calculate, fg="white", bg="#008dff").grid(column=0, row=3)

Label(frame, text="Foot").grid(column=0 ,row=0)
Label(frame, text="Meters").grid(column=0 ,row=1)

foot_input.focus()
root.bind('<Return>', Calculate)
Button(frame, text="Exit", command=quit, fg="white", bg="#CB300F"). grid(column=1, row=3)

root.mainloop()