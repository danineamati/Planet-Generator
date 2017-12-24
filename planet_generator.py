from tkinter import *
from tkinter import font
import random
import math

from planet import *
                                       
class Clouds:
    ''' This class generates the atmosphere of the planet.'''
    def __init__(self, planet, planet_x, planet_y):
        self.rect_width = planet.radius
        self.rect_height = planet.radius / 5
        self.endcirc_radius = self.rect_height / 2
        self.color = "#F8F9F9"
        self.max_cloud_lat = 0.75 * planet.radius
        self.min_cloud_lat = -(0.75 * planet.radius)
        
    def drawClouds(self, x, y):
        ''' Draws the clouds onscreen.'''
        canvas.create_rectangle((x - self.rect_width / 2),\
                                (y - self.rect_height / 2),\
                                (x + self.rect_width / 2),\
                                (y + self.rect_height / 2), fill = self.color,\
                                outline = self.color)
    



if __name__ == '__main__':
    root = Tk()
    width = 1000
    height = 700
    root.geometry('{}x{}'.format(width, height))

    canvas = Canvas(root, width = width, height = height, bg = 'black')
    canvas.pack()
    
    planet_x = 750
    planet_y = 250
    
    planet1 = Planets('Yavin5', canvas)
    planet1.writePlanetSpecs(planet1)
    planet1.drawPlanet(planet_x, planet_y, planet1)

    cloud = Clouds(planet1, planet_x, planet_y)
    cloud.drawClouds(500, 350)

    #print(font.families())
    root.bind('<q>', quit)
    root.mainloop()
