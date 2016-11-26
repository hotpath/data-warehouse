from Tkinter import *
from PIL import ImageTk
from pymongo import MongoClient

class Process:
    def __init__(self):
        self.window = Tk()
        self.rejilla = False
        self.tam_rejilla = 10
        self.canvas_width = 1192
        self.canvas_height = 842
        self.mongo = MongoClient('mongodb://localhost:27017')
        self.db = self.mongo.cein

        self.floors = [
            ImageTk.PhotoImage(file="../floors_img/f0-50.png"),
            ImageTk.PhotoImage(file="../floors_img/f1-50.png"),
            ImageTk.PhotoImage(file="../floors_img/f2-50.png")
        ]

    def checkered(self, canvas):
        # vertical lines at an interval of "line_distance" pixel
        for x in range(self.tam_rejilla, self.canvas_width, self.tam_rejilla):
            canvas.create_line(x, 0, x, self.canvas_height, fill="#476042")
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(self.tam_rejilla, self.canvas_height, self.tam_rejilla):
            canvas.create_line(0, y, self.canvas_width, y, fill="#476042")

    def fill_floor(self, floor_number, data):
        canvas = Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        canvas.create_image(0, 0, image=self.floors[floor_number], anchor=NW)
        canvas.pack()
        if self.rejilla:
            self.checkered(canvas)

        # * densities row col visits floor minute

        for d in data:
            canvas.create_rectangle(d.row, d.col, d.row + self.tam_rejilla, d.col + self.tam_rejilla, width=0,
                                    fill="green",
                                    stipple="gray50")

        # TODO print to file w.postscript(file="file_name.ps", colormode='color')

    def get_data_floor(self, floor, minute=None):

        search = {"floor": floor}
        if minute:
            search.update({"minute": minute})

        data = self.db.densities.find(search)

    def run(self):

        self.fill_floor(1, self.get_data_floor(1))
        self.fill_floor(2, self.get_data_floor(2))
        self.fill_floor(3, self.get_data_floor(3))

        mainloop()


if __name__ == '__main__':
    test_data()
    # v = Process().run()
