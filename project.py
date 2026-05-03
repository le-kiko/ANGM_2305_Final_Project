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

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        screen.fill((0,0,0))

        draw_stars(screen, settings)
        changed = draw_panel(screen, font, width, height, mouse, click,
                             settings, scale)
        if changed == "planets":
            pass
        elif changed == "rings":
            pass
        elif changed == "moons":
            pass
        elif changed == "stars":
            generate_stars(settings, width, height)
        elif changed == "colors":
            pass
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()