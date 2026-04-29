import pygame
import math
import random

settings = {
    "num_planets": 5,
    "has_rings": True,
    "has_moons": True,
    "star_density": 50,
    "color_scheme": 0
}

def draw_button(screen, font, text, x, y, w, h, mouse, click):
    rect = pygame.Rect(x, y, w, h)
    color = (60, 60, 60)

    if rect.collidepoint(mouse):
        color = (100, 100, 100)

    pygame.draw.rect(screen, color, rect, border_radius=6)

    label = font.render(text, True, (255,255,255))
    screen.blit(label, (x + 6, y + 6))

    if rect.collidepoint(mouse) and click:
        return True
    return False

def draw_panel(screen, font, width, height, mouse, click, settings):
    panel_y = height - 80
    pygame.draw.rect(screen, (25, 25, 25), (0, panel_y, width, 80))

    x = 30

    # -------- planets --------
    screen.blit(font.render("Planets", True, (200,200,200)), (x, panel_y + 25))
    x += 80

    if draw_button(screen, font, "-", x, panel_y + 20, 30, 30, mouse, click):
        settings["num_planets"] = max(3, settings["num_planets"] - 1)
    x += 40

    screen.blit(font.render(str(settings["num_planets"]), True, (255,255,255)),
                (x, panel_y + 25))
    x += 40

    if draw_button(screen, font, "+", x, panel_y + 20, 30, 30, mouse, click):
        settings["num_planets"] = min(10, settings["num_planets"] + 1)
    x += 80

    # -------- rings --------
    if draw_button(screen, font,
                   f"Rings: {'ON' if settings['has_rings'] else 'OFF'}",
                   x, panel_y + 20, 130, 30, mouse, click):
        settings["has_rings"] = not settings["has_rings"]
    x += 150

    # -------- moons --------
    if draw_button(screen, font,
                   f"Moons: {'ON' if settings['has_moons'] else 'OFF'}",
                   x, panel_y + 20, 140, 30, mouse, click):
        settings["has_moons"] = not settings["has_moons"]
    x += 160

    # -------- stars --------
    screen.blit(font.render("Stars", True, (200,200,200)), (x, panel_y + 25))
    x += 60

    if draw_button(screen, font, "-", x, panel_y + 20, 30, 30, mouse, click):
        settings["star_density"] = max(10, settings["star_density"] - 10)
    x += 40

    screen.blit(font.render(str(settings["star_density"]), True, (255,255,255))
                , (x, panel_y + 25))
    x += 40

    if draw_button(screen, font, "+", x, panel_y + 20, 30, 30, mouse, click):
        settings["star_density"] = min(200, settings["star_density"] + 10)
    x += 80

    # -------- color --------
    if draw_button(screen, font,
                   f"Theme {settings['color_scheme']}",
                   x, panel_y + 20, 120, 30, mouse, click):
        settings["color_scheme"] = (settings["color_scheme"] + 1) % 5

def main():
    pygame.init()
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h

    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN |
                                     pygame.SCALED)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

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
        draw_panel(screen, font, width, height, mouse, click, settings)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()