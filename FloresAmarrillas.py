import pygame
import math


pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ramo de Flores Amarillas con Bordes")

YELLOW = (255, 204, 0)
ORANGE = (255, 140, 0)
SKIN_COLOR = (255, 228, 196) 
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)

clock = pygame.time.Clock()

def draw_flower(screen, x, y, petal_radius, petal_count, rotation_angle):
    for i in range(petal_count):
        angle = (2 * math.pi / petal_count) * i + rotation_angle
        petal_x = x + math.cos(angle) * (petal_radius * 1.5)
        petal_y = y + math.sin(angle) * (petal_radius * 1.5)
        
        pygame.draw.ellipse(screen, ORANGE, (petal_x - petal_radius - 5, petal_y - petal_radius - 5, (petal_radius * 2) + 10, (petal_radius * 3) + 10))
        pygame.draw.ellipse(screen, YELLOW, (petal_x - petal_radius, petal_y - petal_radius, petal_radius * 2, petal_radius * 3))
    
    pygame.draw.circle(screen, ORANGE, (x, y), petal_radius)

def draw_stem(screen, x, y, length, width, angle):
    end_x = x + length * math.cos(angle)
    end_y = y + length * math.sin(angle)
    pygame.draw.line(screen, GREEN, (x, y), (end_x, end_y), width)

def draw_leaves(screen, x, y, leaf_width, leaf_height, angle):
    leaf1_x = x + 50 * math.cos(angle)
    leaf1_y = y + 50 * math.sin(angle)
    leaf2_x = x + 100 * math.cos(angle)
    leaf2_y = y + 100 * math.sin(angle)
    
    pygame.draw.ellipse(screen, GREEN, (leaf1_x - leaf_width // 2, leaf1_y, leaf_width, leaf_height))
    pygame.draw.ellipse(screen, GREEN, (leaf2_x - leaf_width // 2, leaf2_y, leaf_width, leaf_height))

petal_count = 8
petal_radius = 40
rotation_angle = 0
stem_length = 350
stem_width = 8
leaf_width, leaf_height = 60, 30

flowers = [
    {'x': width // 2 - 100, 'y': height // 2 - 150, 'angle': math.radians(70)},  
    {'x': width // 2 + 100, 'y': height // 2 - 150, 'angle': math.radians(110)},   
    {'x': width // 2, 'y': height // 2 - 200, 'angle': math.radians(90)}          
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKIN_COLOR)

    for flower in flowers:
        draw_stem(screen, flower['x'], flower['y'], stem_length, stem_width, flower['angle'])
        draw_leaves(screen, flower['x'], flower['y'], leaf_width, leaf_height, flower['angle'])
        draw_flower(screen, flower['x'], flower['y'], petal_radius, petal_count, rotation_angle)

    rotation_angle += 0.02 

    pygame.display.flip()

    clock.tick(60)

pygame.quit()