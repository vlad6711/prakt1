import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill([255, 255, 255])  # белый фон. Аналог записи screen.fill('white')
pygame.display.set_caption('Первая программа на pygame')

# # создание фигур с помощью функции pygame.draw
# pygame.draw.circle(screen, 'red', [200, 100], 30, width=0)  # 30-радиус в пикселях, width-ширина контура
# pygame.draw.circle(screen, [255, 154, 15], [100, 400], 50, width=15)
# pygame.draw.circle(screen, '#FFE55F', [400, 300], 100, width=5)
#
# # создание прямоугольника
# pygame.draw.rect(screen, 'yellow', [400, 20, 300, 200], 0)  # [400, 20, 300, 200] - x, y, ширина, высота
#
# # создать пять прямоугольников по размеру и положению прямоугольников
# for i in range(5):
#     top = random.randint(50, 700)
#     left = random.randint(50, 500)
#     w = random.randint(10, 200)
#     h = random.randint(10, 100)
#     color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
#     pygame.draw.rect(screen, color, [top, left, w, h], 4)
#
# # создать произвольную фигуру из линий
# dots = [[221, 432], [225, 331], [133, 342], [141, 310],
#         [51, 230], [74, 217], [58, 153], [114, 164],
#         [123, 135], [176, 190], [159, 77], [193, 93],
#         [230, 28], [267, 93], [301, 77], [284, 190],
#         [327, 135], [336, 164], [402, 153], [386, 217],
#         [409, 230], [319, 310], [327, 342], [233, 331],
#         [237, 432]]
# pygame.draw.lines(screen, 'green', True, dots, 2)  # closed=True первая и последняя точка соединены

# дом
# крыша
roof = [[400, 300], [650, 400], [150, 400]]
pygame.draw.lines(screen, 'blue', True, roof, 6)
# стены
pygame.draw.rect(screen, 'blue', [250, 400, 300, 200], 6)  # [400, 20, 300, 200] - x, y, ширина, высота
# дверь
pygame.draw.rect(screen, 'blue', [290, 450, 100, 150], 6)
pygame.draw.circle(screen, 'blue', [310, 525], 7, width=0)
# окно1
pygame.draw.circle(screen, 'blue', [400, 355], 35, width=6)
window1 = [[400, 325], [400, 385]]
window2 = [[370, 355], [430, 355]]
pygame.draw.lines(screen, 'blue', False, window1, 6)
pygame.draw.lines(screen, 'blue', False, window2, 6)
# окно2
pygame.draw.rect(screen, 'blue', [430, 450, 80, 80], 6)
window1 = [[470, 450], [470, 525]]
window2 = [[430, 490], [507, 490]]
pygame.draw.lines(screen, 'blue', False, window1, 6)
pygame.draw.lines(screen, 'blue', False, window2, 6)

# # яблоко на экране
# apple = pygame.image.load('apple.png')
# screen.blit(apple, [400, 450])  # копирование пикселей с растрового изображения (блитинг)
# pygame.display.flip()  # обновляет монитор
#
# # переместить изображение в новые координаты
# pygame.time.delay(2000)  # 2000мс=2 сек
# pygame.draw.rect(screen, 'white', [400, 450, 100, 100], 0)  # стираем старое яблоко
# screen.blit(apple, [600, 450])  # копирование пикселей с растрового изображения (блитинг)

pygame.display.flip()  # обновляет монитор
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # пришло ли событие нажатия на крестик
            running = False
pygame.quit()  # закрыть окно крестиком
