from vpython import *
from math import sin, cos
import tkinter as tk

# Adjustable Canvas
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Set up canvas with dynamic width and height
scene = canvas(title="SKITM Minor Project", 
               width=screen_width, 
               height=screen_height, 
               background=color.black)


# Create Sun
sun = sphere(pos=vector(0, 0, 0), radius=4, color=color.yellow, emissive=True) # 1392000 km

# Add light
distant_light(direction=vector(1, 1, -1), color=color.white)

# Create a label for the Solar System
label(pos=vector(0, 30, 0), text="Solar System", height=30, color=color.white, box=False)

# Create a label for Sun
label(pos=sun.pos, text="Sun", height=12, color=color.white, box=False)

# Define planets
planets = [
    {"name": "Mercury", "color": color.gray(1), "radius": 1, "orbit_radius": 7, "speed": 0.02}, # 0.05
    {"name": "Venus", "color": vector(1.39,0.69,0.19),"radius": 1.4, "orbit_radius": 11, "speed": 0.012}, # 0.03
    {"name": "Earth", "color": vector(0.4,1.3,0.8), "radius": 1.6, "orbit_radius": 15, "speed": 0.008},# 0.02
    {"name": "Mars", "color": vector(1,0,0), "radius": 1.2, "orbit_radius": 21, "speed": 0.0064},# 0.016
    {"name": "Jupiter", "color": color.orange, "radius": 2.5, "orbit_radius": 24, "speed": 0.004}, # 0.01
    {"name": "Saturn", "color": vector(2.4,1.6,0.9), "radius": 1.7, "orbit_radius": 28, "speed": 0.0032}, # 0.008
    {"name": "Uranus", "color": color.cyan, "radius": 1.8, "orbit_radius": 32, "speed": 0.0024}, # 0.006
    {"name": "Neptune", "color": color.blue, "radius": 1.6, "orbit_radius": 36, "speed": 0.0016} # 0.004
]

# List to store planet objects and labels
planet_objects = []
planet_labels = []

# Create planets
for planet in planets:
    planet_obj = sphere(
        pos=vector(planet["orbit_radius"], 0, 0), 
        radius=planet["radius"],
        color=planet["color"],
        make_trail=True,
        retain=150
    )
    # Initialize angle for orbit
    planet["angle"] = 0
    planet_objects.append(planet_obj)
    
    # Create labels for each planet
    planet_label = label(
        pos=planet_obj.pos + vector(0.5, 0, 0), 
        text=planet["name"], 
        height=12, 
        color=planet["color"], 
        box=False
    )
    planet_labels.append(planet_label)

# Function to create a Flat Saturn's ring
def create_flat_ring(radius, thickness, color):
    # Create a flat ring
    ring_obj = cylinder(
        pos=vector(0, 0, 0), axis=vector(50, 80, 100), radius=radius, 
        length=thickness, color=color
    )
    return ring_obj

# Add flat rings to Saturn with Adjustable Size or Radius
saturn_ring = create_flat_ring(3, 0.04, color.white)

# Create the Moon
earth_moon = sphere(
    pos=vector(planets[2]["orbit_radius"] + 2, 0, 0),  # Position relative to Earth
    radius=0.5,
    color=color.white,
    make_trail=True,
    retain=50
)

# Create a label for the Moon
earth_moon_label = label(
    pos=earth_moon.pos + vector(0.5, 0, 0), 
    text="Moon", 
    height=12, 
    color=color.white, 
    box=False
)

# Render or Animate the Planets
while True:
    rate(60)  # Controls the speed of the environment or Animation
    for i, planet in enumerate(planets):
        planet["angle"] += planet["speed"]  # Update the angle
        x = planet["orbit_radius"] * cos(planet["angle"])
        y = planet["orbit_radius"] * sin(planet["angle"])
        planet_objects[i].pos = vector(x, y, 0)  # Update planet position
        # Update planet name position
        planet_labels[i].pos = planet_objects[i].pos + vector(0.5, 0, 0)
    
    # Update Saturn's ring position to follow Saturn
    saturn_ring.pos = planet_objects[5].pos

    # Update the moon's position to follow Earth
    earth_moon.pos = planet_objects[2].pos + vector(2.5 * cos(2*planets[2]["angle"]), 2.5 * sin(2*planets[2]["angle"]), 0)

    # Update the Moon's label position to follow the Moon
    earth_moon_label.pos = earth_moon.pos + vector(0.5, 0, 0)