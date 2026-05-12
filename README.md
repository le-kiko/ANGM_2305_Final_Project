# PROJECT TITLE: Solar System Generator 

## Demo
Demo Video: <https://youtu.be/HLVf5nrVYvg>

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
- project.py: contains all the code needed to run the program
- space-ambient.mp3: royalty-free sound used as ambient background noise as the
program runs (source: <https://pixabay.com/music/ambient-space-ambient-435262/>
)
- requirements.txt: lists any pip-installable 3rd-party libraries used in the
project
- proposal.md: describes the features, challenges, outcomes, and milestones
used to guide the project's development
- README.md: describes the features, files, design considerations, and future
areas of improvement for the project and contains links to the YouTube video
and GitHub repository
- pfda_finalProject_TatarAnna.mp4: video demonstration of how the project runs

### Design Considerations
In my project design, I decided to draw a sun in the center of the system with
multiple circles and create planets that revolve around the sun on individual
trajectories. The system limits the number of planets that can be generated to
between 3 and 10. It takes user input for whether rings appear in the scene or
not and these rings are randomly applied to one or two planets in the scene.
Similarly, users can control the number of moons, between 0 and 5, that are
once again randomly applied to any of the planets in the scene. Users can also
control star density between the three options of Low (100 stars), Medium (200
stars), and High (400 stars). Planets can also be assigned a color scheme from
the options of Random, Grey, Red, Green, Blue, Purple, and Natural. Finally,
the EXIT button ends the program and takes the user out of the full-screen
display.

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