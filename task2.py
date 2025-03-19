import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Анимация фигур')

shapes = [
    {'type': 'square', 'color': [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 'rect': pygame.Rect(100, 75, 100, 100), 'speed': 2},
    {'type': 'rectangle', 'color': [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 'rect': pygame.Rect(200, 200, 100, 60), 'speed': 2},
    {'type': 'circle', 'color': [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 'rect': pygame.Rect(300, 300, 100, 100), 'speed': 2},
    {'type': 'triangle', 'color': [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 'rect': pygame.Rect(400, 425, 100, 100), 'speed': 2}
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for shape in shapes:
                if shape['rect'].collidepoint(event.pos):
                    shape['color'] = [random.randint(0, 255) for _ in range(3)]

    screen.fill((255, 255, 255))

    for shape in shapes:
        shape['rect'].x += shape['speed']

        if shape['rect'].right >= 800 or shape['rect'].left <= 0:
            shape['speed'] = -shape['speed']
            shape['color'] = [random.randint(0, 255) for _ in range(3)]

        if shape['type'] == 'square':
            pygame.draw.rect(screen, shape['color'], shape['rect'])
        elif shape['type'] == 'rectangle':
            pygame.draw.rect(screen, shape['color'], shape['rect'])
        elif shape['type'] == 'circle':
            pygame.draw.ellipse(screen, shape['color'], shape['rect'])
        elif shape['type'] == 'triangle':
            pygame.draw.polygon(screen, shape['color'], [
                (shape['rect'].left + shape['rect'].width // 2, shape['rect'].top),
                (shape['rect'].left, shape['rect'].bottom),
                (shape['rect'].right, shape['rect'].bottom)
            ])

    pygame.display.flip()

    pygame.time.delay(10)

pygame.quit()
