import tkinter as tk
class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_username = tk.Label(self, text = "nr indeksu")
        self.label_username.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False,height=False)
    root.geometry("500x300")
    root.title("Ps")

    image = tk.PhotoImage(file="./Graphics/background.gif")
    background = tk.Label(root, image=image)
    background.place(x=0, y=0, relwidth=1, relheight=1)


    gui = GUI(root)
    gui.mainloop()