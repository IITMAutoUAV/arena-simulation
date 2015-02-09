# from Tkinter import Tk, Frame, BOTH

# class Example(Frame):
# 	def __init__(self, parent):
# 		Frame.__init__(self, parent, background="pink")
# 		self.parent = parent
# 		self.initUI()

# 	def initUI(self):
# 		self.parent.title("Simple")
# 		self.pack(fill=BOTH, expand=1)

# def main():
# 	root = Tk()
# 	root.geometry("250x150+300+300")
# 	app = Example(root)
# 	root.mainloop()

# if __name__ == '__main__':
# 	main()
# from Tkinter import Tk, Frame, BOTH



# class Example(Frame):
  
#     def __init__(self, parent):
#         Frame.__init__(self, parent, background="white")   
         
#         self.parent = parent
#         self.parent.title("Centered window")
#         self.pack(fill=BOTH, expand=1)
#         self.centerWindow()

#     def centerWindow(self):
      
#         w = 400
#         h = 400

#         sw = self.parent.winfo_screenwidth()
#         sh = self.parent.winfo_screenheight()
        
#         x = (sw - w)/2
#         y = (sh - h)/2
#         self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

# def main():
  
#     root = Tk()
#     ex = Example(root)
#     root.mainloop()  


# if __name__ == '__main__':
#     main()
# from Tkinter import Tk, BOTH
# from ttk import Frame, Button, Style


# class Example(Frame):
  
#     def __init__(self, parent):
#         Frame.__init__(self, parent)   
         
#         self.parent = parent
        
#         self.initUI()
        
#     def initUI(self):
      
#         self.parent.title("Quit button")
#         self.style = Style()
#         self.style.theme_use("default")
#         # self.style.theme_use("clam")
#         # self.style.theme_use("classic")
#         # self.style.theme_use("alt")

#         self.pack(fill=BOTH, expand=1)

#         quitButton = Button(self, text="Quit",
#             command=self.quit)
#         quitButton.place(x=50, y=50)


# def main():
  
#     root = Tk()
#     root.geometry("250x150+300+300")
#     app = Example(root)
#     root.mainloop()  


# if __name__ == '__main__':
#     main() 

from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Buttons")
        # self.style = Style()
        # self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)
        
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
              

def main():
  
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()