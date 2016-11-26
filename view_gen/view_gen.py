#!/usr/bin/python

from Tkinter import *
from sympy.functions.combinatorial.numbers import fibonacci

from PIL import ImageTk
from pymongo import MongoClient
import os
import datetime
import time


class ViewGen:
    def __init__(self):
        self.window = Tk()
        self.rejilla = False
        self.tam_rejilla = 10
        self.canvas_width = 1192
        self.canvas_height = 842
        self.conversion_factor = 2
        try:
            self.ouput_file = int(sys.argv[2])
        except IndexError:
            self.ouput_file = 0

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
        totalVisits = 0;
        for d in data:
          totalVisits+= d['visits']
        for d in data:
            row = d['row'] / 2
            col = d['col'] / 2
            visitasCelda = d['visits'] / totalVisits
            print(visitasCelda)
            canvas.create_rectangle(row, col, row + self.tam_rejilla,
                                    col + self.tam_rejilla, width=0,
                                    fill="green",
                                    stipple="gray50")
        if self.ouput_file == 1:
            self.save_to_file(canvas)

    def save_to_file(self, canvas):

        canvas.postscript()
        canvas.postscript(file='tmp.ps', x=0, y=0, height=self.canvas_height, width=self.canvas_width)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
        filename = 'image' + st + '.png'
        os.system('convert -density 300 tmp.ps -resize ' + str(self.canvas_width) + 'x' + str(
            self.canvas_height) + ' ' + 'output/' + filename)

    def get_data_floor(self, floor, minute=None):

        search = {"floor": floor}
        if minute:
            search.update({"minute": minute})

        data = self.db.densities.find(search)

        return data

    def run(self):

        try:

            floor = int(sys.argv[1])
            if floor in [0, 1, 2]:
                self.fill_floor(floor, self.get_data_floor(floor))
            else:
                raise IndexError
            if self.ouput_file != 1:
                mainloop()
        except IndexError:
            print("That floor not exists ....")


if __name__ == '__main__':
    p = ViewGen()
    p.run()
