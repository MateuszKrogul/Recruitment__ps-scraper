import tkinter as tk
class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.image = tk.PhotoImage(file="./Graphics/background.gif")
        self.background = tk.Label(root, image=self.image, compound=tk.CENTER)
        self.background.place(x=0, y=50) # x=0, y=0, relwidth= 1, relheight= 1

        #entry_username = tk.Entry(self)
        #entry_username.pack()

        self.c = tk.Canvas(master=root)
        self.c.place(x= 0, y=0)
        self.c.create_text(200,20, text= "test",width=0)
        #label_username = tk.Label(self.c, text = "nr indeksu")
        #label_username.place(x=0, y=0) # x=0 , y=0

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False,height=False)
    root.geometry("600x400") #500x300
    root.wm_attributes('-transparent', 'True')
    root.title("Ps")

    #image = tk.PhotoImage(file="./Graphics/background.gif")

    #window = tk.Canvas(root, width=500, height=300)
    #window.create_image(0,0, anchor = tk.NW, image=image)
    #window.pack()

    #background = tk.Label(root, image=image)
    #background.place(x=0, y=0, relwidth=1, relheight=1)

    #app = tk.Frame(root)
    #app.mainloop()
    gui = GUI(root)
    gui.mainloop()