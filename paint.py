from tkinter import *
from tkinter import ttk, colorchooser
from tkinter.filedialog import asksaveasfile

class paintapp:
    def __init__(self, master):
        self.master = master
        self.colorfg = 'black'
        self.colorbg = 'white'
        self.oldx = None
        self.oldy = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, e):
        if self.oldx and self.oldy:
            self.c.create_line(self.oldx, self.oldy, e.x, e.y, width=self.penwidth, fill=self.colorfg,capstyle=ROUND, smooth=True)
        self.oldx = e.x
        self.oldy = e.y

    def reset(self,e):
        self.oldx = None
        self.oldy = None

    def changeW(self, e):
        self.penwidth = e

    def clear(self):
        self.c.delete(ALL)

    def changefg(self):
        self.colorfg = colorchooser.askcolor(color=self.colorfg)[1]

    def changebg(self):
        self.colorbg = colorchooser.askcolor(color=self.colorbg)[1]
        self.c['bg'] = self.colorbg

    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Pen Width:', font=('arial 16')).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.changeW, orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack(side=LEFT)

        self.c = Canvas(self.master, width=500, height=400, bg=self.colorbg, )
        self.c.pack(fill=BOTH, expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Brush Color', command=self.changefg)
        colormenu.add_command(label='Background Color', command=self.changebg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Exit', command=self.master.destroy)

if __name__ == '__main__':
    window = Tk()
    paintapp(window)
    window.title('Paint App')
    window.mainloop()

