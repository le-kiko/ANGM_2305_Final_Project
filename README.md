# ANGM_2305_Final_Project
Final project for ANGM 2305 (Programming for Digital Arts)

# Title: Solar System Scene Generator 

## Description
This project will generate a solar system scene with 3D, rotating planets,
taking in user input to customize what is generated. It is relevant to digital
arts and media because it combines generation of art with animation and user
interaction and control.

## Features
- Effect of color of light from sun on objects in the scene as they move:
	- Based on the sunlight, I will adjust the shading and color tint on each
    celestial object.
    - I would adjust alpha and RGB values and apply them to surfaces with
    pygame's Surface class.
- Texture and features of the planets and other celestial bodies: 
	- For each celestial body, the exterior framework is set and a texture is
    applied to match whether the body is a planet or moon.
    - I would use pygame's draw module and image function to create the planets
    and apply a texture to them.
- Rotation of celestial bodies:
	- Each object has an orbit or trajectory that it follows and an axis that
    it spins or rotates around.
    - I would import pygame and math to use pygame's time module to update dt
    and math to plan an orbital path and rotation angle.
- Panel with buttons or other controls to take user input:
    - Buttons or controls will respond to user mouse input and result in the
    desired action being performed.
    - I would use pygame.MOUSEBUTTONDOWN or similar commands to control the
    program's response to actions performed by the user.

## Outcomes
Ideal Outcome:
- The ideal outcome for this project would be a space scene that generates
planets, stars, and other celestial bodies while accepting user input for the
number of planets in the scene, whether some of the planets have rings and
moons or not, the density of stars in the background, and the general color
scheme of the scene.

Minimal Viable Outcome:
- The minimal viable outcome for this project would be a space scene that
generates 3D planets and other celestial bodies that rotate in space when the
program is run.