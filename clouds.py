from tkinter import *
from tkinter import font
import random
import math

from planet import *
                                       
class Clouds:
    ''' This class generates the atmosphere of the planet.'''
    def __init__(self, planet, planet_x, planet_y, canvas):
        self.planet = planet
        self.planet_x = planet_x
        self.planet_y = planet_y
        self.canvas = canvas
        
        self.rect_width = planet.radius
        self.rect_height = planet.radius / 5
        self.endcirc_radius = self.rect_height / 2
        self.color = "#F8F9F9"
        self.max_cloud_lat = 0.75 * planet.radius
        self.min_cloud_lat = -(0.75 * planet.radius)
        
    def drawClouds(self, x, y):
        ''' Draws the clouds onscreen.'''
        self.canvas.create_rectangle((x - self.rect_width / 2),\
                                (y - self.rect_height / 2),\
                                (x + self.rect_width / 2),\
                                (y + self.rect_height / 2), fill = self.color,\
                                outline = self.color)
