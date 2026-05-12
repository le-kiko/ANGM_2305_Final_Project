# PROJECT TITLE: Solar System Generator 

## Demo
Demo Video: <>

## GitHub Repository
GitHub Repo: <https://github.com/le-kiko/ANGM_2305_Final_Project.git>

## Description
This project generates a solar system scene with 3D, rotating planets, taking 
user input to customize what is generated. It is relevant to digital
arts and media because it combines generation of art with animation and user
interaction and control.

### Features
- The shading on each celestial object adjusts based on its position relative
to the sun. 
- For each celestial body, the exterior framework is set and a color is applied
to match whether the body is a planet or moon.
- Each object has an orbit or trajectory that it follows and an axis that it
spins or rotates around.
- Buttons in the panel respond to user mouse input and result in the desired
action being performed. They control: the number of planets in the scene,
whether rings appear in the scene or not, the number of moons in the scene, the
density of stars in the scene, and the color scheme applied to planets.

### Files
The project.py file contains all the code needed to run the program. The
mp3 file is the royalty-free sound used as ambient background noise while the
program runs (source: [https://pixabay.com/music/ambient-space-ambient-435262/]
(https://pixabay.com/music/ambient-space-ambient-435262/)).The requirements.txt
file lists any pip-installable 3rd-party libraries used in the project. The
proposal and README markdown files are included to fulfill project submission
requirements.

INCLUDE YOUTUBE VIDEO FILE

### Design Considerations
To be able to manage creating planets and moons based on user input, I decided
to use classes so applying the different features to different planets could be
done relatively easily. I also created the `add_perspective` function to add a
z dimension to make the scene look 3D. Although the program runs full-screen, I
had to use a scale factor to ensure the panel and its buttons will look good on
other screen sizes as well.

### Future Areas of Improvement
Areas that I could improve on this project mainly relate to what other options
I could provide for user input. For example, I could allow greater control over
the number of rings that show up in the scene, like for planets and moons, or I
could include an option to have asteroids randomly cross the scene. I could
also allow the user more control over their view and let them zoom in or out or
move themselves around the scene.