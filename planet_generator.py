from tkinter import *
from tkinter import font
import random
import math

class Planets:
    ''' This class generates a planet based on random factors.'''
    def __init__(self, name):
        ''' Creates a planet from randomly determined features.'''
        self.name = name
        self.radius = random.randint(50, 250)
        
        self.day = random.random() * 30
        if self.day == 0: # Ensure day + night > 0
            self.night = (random.random() + 0.1) * 30
        else:
            self.night = random.random() * 30
        self.daynight = self.day + self.night
        
        self.sea_level = random.random() # Percentage of water
        # 0 == NO WATER!!! and 1 == NO LAND!!!
        
        self.vege_amt = self.sea_level * random.random()
        # vege_amt = % of land covered by vegetation
        self.vege_type = random.choice(['Carnivorus Plants',\
                                        'Tentacles','Metal Trees',\
                                        'Organic Spikes','Giant Lilypads',\
                                        'Trees'])
        self.urban = random.random()
        # 0 = NO CITIES, 1 = CORUSCANT
        ages = ['Stone Age',\
                'Iron Age',\
                'Industrial Age',\
                'Automation Age',\
                'Artificial Age',\
                'Type 1 Civilization']
        self.tech = random.choice(ages[:int(self.urban * 6) + 1])

    def __str__(self):
        '''Return a string representing the planet.'''
        Planet_str = '''
                        Name: {}
                        Radius: {} km
                        Day: {} Earth Hours
                        Night: {} Earth Hours
                        Sol: {} Earth Hours (Total)
                        Sea Level: {}% water
                        Vegetation Amount: {}% vegetated
                        Vegetation Type: {}
                        Urbanization: {}% of land urbanized
                        Technology: {}
                        '''.format(self.name, self.radius * 70,\
                                   '%.2f' % self.day,\
                                   '%.2f' % self.night,\
                                   '%.2f' % self.daynight,\
                                   '%.2f' % self.sea_level,\
                                   '%.2f' % self.vege_amt,\
                                   self.vege_type,\
                                   '%.2f' % self.urban,\
                                   self.tech)
        return Planet_str
                                       
class Clouds:
    

def drawCircle(x, y, r, color):
    ''' This function will draw a circle on the canvas. The center is at x, y
    and the r is the radius. There is also a color argument the determines the
    color of the circle.
    The function returns the handle of the circle object.'''
    circle = canvas.create_oval(x - r, y - r, x + r, y + r,\
                                fill = color, outline = color)
    circles.append(circle)
    return circle

def randomCircles(x, y, rMax, planet):
    ''' This function creates random circles at random locations on the planet
    of designated color'''
    land_color = 'NavajoWhite2'
    vege_color = {
            'Carnivorus Plants' : 'medium aquamarine',
            'Tentacles' : 'indian red',
            'Metal Trees' : '#979A9A',
            'Organic Spikes' : 'dark olive green',
            'Giant Lilypads' : 'dark sea green',
            'Trees' : 'dark green'                        
    }
    
    # Generates an integer number of circles based on planet sea level
    # 33 is completly arbitrary
    numCircles = int((1 - planet.sea_level) * 33)
    vege_specific = vege_color[planet.vege_type]

    for circle in range(numCircles):
        r_circle = random.randint(10, int(0.5 * rMax))
        # r_1 is the distance from the center of the planet to the center of
        # the randomly generated circle
        r_1 = (random.random() + 0.25) * (rMax - r_circle - (0.25 * (rMax - r_circle)))
        theta = random.random() * (2 * math.pi)
        delta_x = r_1 * math.cos(theta)
        delta_y = -r_1 * math.sin(theta)
        circ_color = land_color
        if (random.random() * planet.vege_amt) > (planet.vege_amt * planet.vege_amt):
            circ_color = vege_specific
            
        circ_handle = drawCircle(x + delta_x, y + delta_y, r_circle, circ_color)
        circles.append(circ_handle)

def polarCaps(x, y, r, planet):
    ''' This function takes a planet and generates the polar caps of the
    planet.'''
    pass

if __name__ == '__main__':
    root = Tk()
    width = 1000
    height = 700
    root.geometry('{}x{}'.format(width, height))

    canvas = Canvas(root, width = width, height = height, bg = 'black')
    canvas.pack()

    circles = []
    planet_x = 750
    planet_y = 250
    planet_r = 200
    drawCircle(planet_x, planet_y, planet_r, 'RoyalBlue3')
    
    planet1 = Planets('NO')
    canvas.create_text(200, 175, text = str(planet1),\
                       fill = 'pale turquoise',\
                       font = font.Font(family = 'Copperplate Gothic Bold',\
                                        size = 11))
    randomCircles(planet_x, planet_y, planet_r, planet1)

    #print(font.families())
    root.bind('<q>', quit)
    root.mainloop()
