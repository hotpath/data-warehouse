from Tkinter import *
from PIL import ImageTk
#import Image, ImageTk, Tkinter
#import matplotlib.pyplot as plt
#import matplotlib.patches as patches

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


master = Tk()
tam_rejilla = 10
canvas_width = 1192
canvas_height = 842 
num_cuadros_x = canvas_width / tam_rejilla
num_cuadros_y = canvas_height / tam_rejilla
num_cuadros = num_cuadros_x * num_cuadros_y
#print (num_cuadrados)
print (num_cuadros)
#num_cuadrados=  int( canvas_width /  canvas_height) * tam_rejilla
#print (num_cuadrados)
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)


image = ImageTk.PhotoImage(file = "f0-50.png")
w.create_image(0, 0, image = image, anchor = NW)
for i in range(num_cuadros):
	 rec = w.create_rectangle(i*tam_rejilla, i*tam_rejilla, i*(tam_rejilla+2),i*(tam_rejilla+2), width=0, fill = "red", stipple="gray50")
	# rec.set_alpha = 2
#w.create_rectangle(20, 20, 20+tam_rejilla, 20+tam_rejilla, width=0, fill='red')
w.pack()
rec = w.create_rectangle(500, 500, 500+tam_rejilla, 500 +tam_rejilla , width=0, fill = "green", stipple="gray50")
# lista (cuad,num_personas)
w.postscript(file="file_name.ps", colormode='color')

#checkered(w,tam_rejilla)

mainloop()


