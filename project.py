import pygame
import math
import random

settings = {
    "num_planets": 5,
    "has_rings": True,
    "num_moons": 3,
    "star_density": "Medium",
    "color_schemes": ["Random", "Grey", "Red", "Green", "Blue", "Purple",
                      "Natural"],
    "color_scheme_index": 0,
    "stars": []
}

def update_stars(settings):
    if settings["star_density"] == "Low":
        return 100
    elif settings["star_density"] == "Medium":
        return 200
    elif settings["star_density"] == "High":
        return 400

def generate_stars(settings, width, height):
    count = update_stars(settings)
    settings["stars"] = [(random.randint(0, width), random.randint(0, height -
                         100)) for i in range(count)]

def draw_stars(screen, settings):
    for star in settings["stars"]:
        pygame.draw.circle(screen, (255,255,255), star, 1)

def set_color(settings):
    scheme = settings["color_schemes"][settings["color_scheme_index"]]
    if scheme == "Red":
        return (random.randint(150,255), random.randint(50,100),
                random.randint(50,100))
    elif scheme == "Green":
        return (random.randint(50,100), random.randint(150,255),
                random.randint(50,100))
    elif scheme == "Blue":
        return (random.randint(50,100), random.randint(50,100),
                random.randint(150,255))
    elif scheme == "Purple":
        return (random.randint(120,200), random.randint(50,100),
                random.randint(150,255))
    elif scheme == "Grey":
        grey_color = random.randint(100,200)
        return (grey_color, grey_color, grey_color)
    elif scheme == "Random":
        return (random.randint(50,255), random.randint(50,255),
                random.randint(50,255))
    else:
        natural_colors = [(200,180,120), (150,100,80), (100,150,255),
                          (180,140,100), (120,200,120), (200,160,120)]
        chosen = random.choice(natural_colors)
        return (chosen)

def draw_button(screen, font, text, x, y, w, h, mouse, click, scale):
    def ui(value):
        return int(value * scale)
    rect = pygame.Rect(x, y, w, h)
    color = (60, 60, 60)

    if rect.collidepoint(mouse):
        color = (100, 100, 100)

    pygame.draw.rect(screen, color, rect, border_radius=ui(6))

    label = font.render(text, True, (255,255,255))
    screen.blit(label, (x + ui(6), y + ui(6)))

    if rect.collidepoint(mouse) and click:
        return True
    return False

def draw_panel(screen, font, width, height, mouse, click, settings, scale):
    def ui(value):
        return int(value * scale)
    
    panel_y = height - ui(80)
    pygame.draw.rect(screen, (25, 25, 25), (0, panel_y, width, ui(80)))
    
    x = ui(30)

    # -------- planets --------
    screen.blit(font.render("Planets", True, (200,200,200)), (x, panel_y +
                                                              ui(25)))
    x += ui(80)

    if draw_button(screen, font, "-", x, panel_y + ui(20), ui(30), ui(30),
                   mouse, click, scale):
        settings["num_planets"] = max(3, settings["num_planets"] - 1)
        return "planets"
    x += ui(40)

    screen.blit(font.render(str(settings["num_planets"]), True, (255,255,255)),
                (x, panel_y + ui(25)))
    x += ui(40)

    if draw_button(screen, font, "+", x, panel_y + ui(20), ui(30), ui(30),
                   mouse, click, scale):
        settings["num_planets"] = min(10, settings["num_planets"] + 1)
        return "planets"
    x += ui(60)

    # -------- rings --------
    if draw_button(screen, font,
                   f"Rings: {'ON' if settings['has_rings'] else 'OFF'}", x,
                   panel_y + ui(20), ui(130), ui(30), mouse, click, scale):
        settings["has_rings"] = not settings["has_rings"]
        return "rings"
    x += ui(150)

    # -------- moons --------
    screen.blit(font.render("Moons", True, (200,200,200)), (x, panel_y +
                                                            ui(25)))
    x += ui(70)

    if draw_button(screen, font, "-", x, panel_y + ui(20), ui(30), ui(30),
                   mouse, click, scale):
        settings["num_moons"] = max(0, settings["num_moons"] - 1)
        return "moons"
    x += ui(40)

    screen.blit(font.render(str(settings["num_moons"]), True, (255,255,255)),
                (x, panel_y + ui(25)))
    x += ui(40)

    if draw_button(screen, font, "+", x, panel_y + ui(20), ui(30), ui(30),
                   mouse, click, scale):
        settings["num_moons"] = min(5, settings["num_moons"] + 1)
        return "moons"
    x += ui(60)

    # -------- stars --------
    if draw_button(screen, font, f"Stars: {settings['star_density']}", x,
                   panel_y + ui(20), ui(150), ui(30), mouse, click, scale):
        if settings["star_density"] == "Low":
            settings["star_density"] = "Medium"
        elif settings["star_density"] == "Medium":
            settings["star_density"] = "High"
        else:
            settings["star_density"] = "Low"
        return "stars"
    x += ui(170)

    # -------- color --------
    current_scheme = settings["color_schemes"][settings["color_scheme_index"]]
    if draw_button(screen, font, f"Theme: {current_scheme}", x, panel_y +
                   ui(20), ui(160), ui(30), mouse, click, scale):
        settings["color_scheme_index"] = (settings["color_scheme_index"]
                                          + 1) % len(settings["color_schemes"])
        return "colors"

    return None

def add_perspective(x, y, z, cx, cy):
    scale = 800 / (800 + z)
    return int(cx + x * scale), int(cy + y * scale), scale

def rotate_y(x, y, z, angle):
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return x * cos_a - z * sin_a, y, x * sin_a + z * cos_a

def draw_sphere(screen, cx, cy, world_x, world_y, world_z, rotation, radius,
                color):
    steps = 16

    for i in range(steps):
        theta = math.pi * i / steps
        for j in range(steps):
            phi = 2 * math.pi * j / steps

            x = radius * math.sin(theta) * math.cos(phi)
            y = radius * math.cos(theta)
            z = radius * math.sin(theta) * math.sin(phi)

            x, y, z = rotate_y(x, y, z, rotation)

            x += world_x
            y += world_y
            z += world_z

            nx = math.sin(theta) * math.cos(phi)
            ny = math.cos(theta)
            nz = math.sin(theta) * math.sin(phi)
            nx, ny, nz = rotate_y(nx, ny, nz, rotation)

            light_x = -world_x
            light_y = -world_y
            light_z = -world_z
            light_length = math.sqrt(light_x**2 + light_y**2 + light_z**2)

            light_x /= light_length
            light_y /= light_length
            light_z /= light_length
                
            diffuse = max(0, nx * light_x + ny * light_y + nz * light_z)
            ambient = 0.25
            brightness = ambient + (0.75 * diffuse)
            brightness = min(1, brightness)
            shaded = (int(color[0] * brightness), int(color[1] * brightness),
                      int(color[2] * brightness))
                    
            px, py, scale = add_perspective(x, y, z, cx, cy)
            pygame.draw.circle(screen, shaded, (px, py), max(1, int(2 *
                                                                    scale)))
            
def draw_ring(screen, px, py, scale, radius, tilt, color, front=False):
    ring_w = int(radius * scale)
    ring_h = max(1, int(radius * tilt * scale))
    rect = pygame.Rect(px - ring_w, py - ring_h // 2, ring_w * 2, ring_h)

    if front:
        start_angle = 0
        end_angle = math.pi
    else:
        start_angle = math.pi
        end_angle = 2 * math.pi

    pygame.draw.arc(screen, color, rect, start_angle, end_angle, 2)

class Moon:
    def __init__(self, orbit_radius):
        self.orbit_radius = orbit_radius
        self.orbit_angle = random.random() * 6

    def update(self, dt):
        self.orbit_angle += 0.05 * dt

    def draw(self, screen, cx, cy, planet_x, planet_y, planet_z, planet_rot,
             planet_radius):
        x = planet_x + self.orbit_radius * math.cos(self.orbit_angle)
        z = planet_z + self.orbit_radius * math.sin(self.orbit_angle)

        moon_px, moon_py, moon_scale = add_perspective(x, planet_y, z, cx, cy)
        planet_px, planet_py, planet_scale = add_perspective(planet_x, planet_y
                                                            , planet_z, cx, cy)

        dx = moon_px - planet_px
        dy = moon_py - planet_py
        dist = math.sqrt(dx**2 + dy**2)

        if z > planet_z and dist < planet_radius * planet_scale:
            return

        draw_sphere(screen, cx, cy, x, planet_y, z, planet_rot, 4,
                    (170,170,170))

class Planet:
    def __init__(self, orbit_radius):
        self.orbit_radius = orbit_radius
        self.orbit_angle = random.random() * 6

        self.radius = random.randint(10, 25)
        self.color = set_color(settings)
        
        self.rotation = 0
        self.moons = []
        self.has_ring = False

    def update(self, dt):
        self.orbit_angle += 0.01 * dt
        self.rotation += 0.02 * dt

        for moon in self.moons:
            moon.update(dt)

    def get_position(self):
        a = self.orbit_radius
        b = int(a * 0.75)

        x = a * math.cos(self.orbit_angle)
        z = b * math.sin(self.orbit_angle)

        y = 25 * math.sin(self.orbit_angle * 2)

        return x, y, z

    def draw(self, screen, cx, cy):
        x, y, z = self.get_position()
        px, py, scale = add_perspective(x, y, z, cx, cy)
        base_r = self.radius + 12
        tilt = 0.35

        if settings["has_rings"] and self.has_ring:
            for i in range(5):
                color = (min(255, 170 + i * 5), min(255, 160 + i * 4),
                         min(255, 130 + i * 3))
                draw_ring(screen, px, py, scale, base_r + i * 2, tilt, color,
                          front=False)
        
        draw_sphere(screen, cx, cy, x, y, z, self.rotation, self.radius,
                    self.color)
        
        if settings["has_rings"] and self.has_ring:
            for i in range(5):
                color = (min(255, 170 + i * 5), min(255, 160 + i * 4),
                         min(255, 130 + i * 3))
                draw_ring(screen, px, py, scale, base_r + i * 2, tilt, color,
                          front=True)

        for moon in self.moons:
            moon.draw(screen, cx, cy, x, y, z, self.rotation, self.radius)

def get_planet_depth(planet):
    return planet.get_position()[2]

def get_depth(obj):
    return obj[1]

def create_planets():
    planets = [Planet(120 + i * 80) for i in range(settings["num_planets"])]

    if settings["has_rings"] and len(planets) > 0:
        ring_count = random.randint(1, min(2, len(planets)))
        ring_planets = random.sample(planets, ring_count)

        for planet in ring_planets:
            planet.has_ring = True

    remaining_moons = settings["num_moons"]
    while remaining_moons > 0:
        planet = random.choice(planets)
        planet.moons.append(Moon(random.randint(30,60)))
        remaining_moons -= 1

    return planets

def draw_sun(screen, cx, cy):
    px, py, unused = add_perspective(0, 0, 0, cx, cy)

    for i in range(60, 0, -1):
        alpha = i / 60
        color = (int(255 * alpha), int(180 * alpha), int(60 * alpha))
        pygame.draw.circle(screen, color, (px, py), i)

    pygame.draw.circle(screen, (255,230,120), (px, py), 40)

def main():
    pygame.init()
    info = pygame.display.Info()
    base_width = 1920
    width, height = info.current_w, info.current_h
    scale = width / base_width

    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN |
                                     pygame.SCALED)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", int(20 * scale))

    generate_stars(settings, width, height)
    planets = create_planets()
    cx, cy = width // 2, height // 2
    
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        click = False
        dt = clock.tick(60) / 16.67

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        screen.fill((0,0,0))

        draw_stars(screen, settings)
        for planet in planets:
            planet.update(dt)
        objects = []

        for planet in planets:
            x, y, z = planet.get_position()
            objects.append(("planet", z, planet))
        objects.append(("sun", 0, None))
        objects.sort(key=get_depth, reverse=True)

        for obj in objects:
            if obj[0] == "sun":
                draw_sun(screen, cx, cy)
            else:
                obj[2].draw(screen, cx, cy)

        changed = draw_panel(screen, font, width, height, mouse, click,
                             settings, scale)
        if changed == "planets":
            planets = create_planets()
        elif changed == "rings":
            pass
        elif changed == "moons":
            planets = create_planets()
        elif changed == "stars":
            generate_stars(settings, width, height)
        elif changed == "colors":
            planets = create_planets()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()