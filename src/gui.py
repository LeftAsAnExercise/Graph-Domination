import tkinter as tk

class ChessBoard(tk.Frame):
	def __init__(self, master, num, SIZE=64):
		super().__init__(master)
		self.master = master
		self.pack()
		self.canvas = tk.Canvas(master)
		color = 'white'
		for y in range(num):
			for x in range(num):
				x1 = x * SIZE
				y1 = y * SIZE
				x2 = x1 + SIZE
				y2 = y1 + SIZE
				self.canvas.create_rectangle((x1, y1, x2, y2), fill=color)
				if color == 'white':
					color = 'black'
				else:    
					color = 'white'

			if color == 'white':
				color = 'black'
			else:    
				color = 'white'
		self.canvas.pack()

if __name__ == '__main__':
	master = tk.Tk()
	board = ChessBoard(master, 10)
	master.mainloop()
