from Tkinter import Tk, Frame, BOTH

class Widget(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background="black")
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title('IARC Arena Simulation')
		self.pack(fill=BOTH, expand=1)
		sw = self.parent.winfo_screenwidth()*0.9
		sh = self.parent.winfo_screenheight()*0.9
		x = self.parent.winfo_screenwidth()*0.05
		y = self.parent.winfo_screenheight()*0.05
		self.parent.geometry('%dx%d+%d+%d' % (sw, sh, x, y))

def main():
	root = Tk()
	mainWindow = Widget(root)
	root.mainloop()

main()