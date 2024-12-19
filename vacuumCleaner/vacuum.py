from vpython import *
import random

# Scene settings
#Sets the title, size, background color, and center of the 3D scene.
scene.title = "3D Vacuum Cleaner Simulation"
scene.width = 800
scene.height = 600
scene.background = color.white
scene.center = vector(0, 0, 0)

# Ground/Room setup
#Creates a gray rectangular ground on which the simulation occurs.
ground = box(pos=vector(0, -0.1, 0), size=vector(10, 0.2, 10), color=color.gray(0.6))

# Vacuum cleaner components
# The main red body of the vacuum cleaner.
vacuum_body = box(pos=vector(0, 0.5, 0), size=vector(1, 0.5, 0.7), color=color.red)
# A blue cylinder acting as the vacuum's cleaning head.
vacuum_head = cylinder(pos=vector(0, 0.5, -0.6), axis=vector(0, 0, -0.5), radius=0.3, color=color.blue)
#Adds four black wheels to the vacuum cleaner.
wheels = [
    cylinder(pos=vector(0.4, 0.2, 0.3), axis=vector(0, 0.2, 0), radius=0.2, color=color.black),
    cylinder(pos=vector(-0.4, 0.2, 0.3), axis=vector(0, 0.2, 0), radius=0.2, color=color.black),
    cylinder(pos=vector(0.4, 0.2, -0.3), axis=vector(0, 0.2, 0), radius=0.2, color=color.black),
    cylinder(pos=vector(-0.4, 0.2, -0.3), axis=vector(0, 0.2, 0), radius=0.2, color=color.black),
]

# Dust particles
#Creates 20 dust particles at random positions within the region (-4, 4) on the x and z axes.
particles = []
brown_color = vector(0.6, 0.3, 0)  #Define brown color as a color vector
for i in range(20):
    pos_x = random.uniform(-4, 4)
    pos_z = random.uniform(-4, 4)
    particles.append(sphere(pos=vector(pos_x, 0.1, pos_z), radius=0.1, color=brown_color))

# Vacuum movement variables
speed = 0.05
direction = vector(1, 0, 0)  # Initial direction
vacuum_position = vacuum_body.pos

# Vacuum cleaner movement function
def move_vacuum():
    global vacuum_position
    # Move the vacuum forward
    new_pos = vacuum_body.pos + direction * speed
     # Check boundaries to keep the vacuum within the block
    if -7.5 <= new_pos.x <= 7.5 and -7.5 <= new_pos.z <= 7.5:
        vacuum_body.pos = new_pos
        vacuum_head.pos += direction * speed
        for wheel in wheels:
           wheel.pos += direction * speed
    vacuum_position = vacuum_body.pos

# Cleaning function
def clean_particles():
    global particles
    for particle in particles[:]: #Iterate over a acopy of the list
        distance_to_vacuum = mag(particle.pos - vacuum_position)
        if distance_to_vacuum < 0.7:  # Vacuum range
            particle.visible = False  # Hide the particle
            particles.remove(particle) #Remove the particle from the list
            break

# Scene instructions
instructions = label(pos=vector(0, 3, 0), text="Arrow Keys to move the vacuum", color=color.black)

# Key press control
#Changes the direction of the vacuum cleaner based on the arrow key pressed.
def control_vacuum(evt):
    global direction
    key = evt.key
    if key == 'up':
        direction = vector(0, 0, -1)
    elif key == 'down':
        direction = vector(0, 0, 1)
    elif key == 'left':
        direction = vector(-1, 0, 0)
    elif key == 'right':
        direction = vector(1, 0, 0)

scene.bind('keydown', control_vacuum)

# Main animation loop
#Continuously moves the vacuum cleaner and checks for nearby particles to clean at 60 frames per second.
while True:
    rate(60)
    move_vacuum()
    clean_particles()
