# Title: Solar System Scene Generator 

## Repository
<https://github.com/le-kiko/ANGM_2305_Final_Project.git>

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

## Challenges
- Learn how to build a 3D object in space.
- Learn how to rotate a 3D object in space around itself and a center point.
- Learn how to assign a color scheme to the objects from user input.
- Learn how to update the scene in real time based on user input.
- Learn how to create buttons or similar controls for user input while the
program is running.

## Outcomes
Ideal Outcome:
- The ideal outcome for this project would be a space scene that generates
spaceships, planets, stars, and other celestial bodies while accepting user
input for the number of planets in the scene, whether some of the planets have
rings and moons or not, the density of stars in the background, and the general
color scheme of the scene.

Minimal Viable Outcome:
- The minimal viable outcome for this project would be a space scene that
generates 3D planets and other celestial bodies that rotate in space when the
program is run.

## Milestones

- Week 1
  1. Research how intended functionality can be achieved through Python
  functions, classes, and commands.
  2. Set up scene surface and background and create full screen display.
  3. Create objects and textures for planets and set up rotation.

- Week 2
  1. Set up effect of light from Sun on surfaces of planets based on the angle
  of rotation of planets relative to the Sun.
  2. Tweak extra additions to celestial bodies such as rings or moons to also
  rotate and have proper lighting.

- Week 3
  1. Research user controls in Python and plan how to implement them for the
  different parameters of control in the panel through UI (User Interface)
  interaction.
  2. Develop code for an UI to allow users to control color scheme of the
  scene, number of planets, number of rings and/or moons, and density of
  background stars.

- Week 4 (Final)
  1. Check that all elements function and have reached functionality at the
  level of the ideal outcome.
  2. Fix any part of the code whose behavior doesn't match or reach the level
  of the ideal outcome.
  3. Add any final touches or details and validate that the final code output
  matches the ideal outcome output.