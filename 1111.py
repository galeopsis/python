import pygame
import random

pygame.init()

w = 800
h = 600

screen = pygame.display.set_mode((w, h))

cookie = pygame.image.load('cookie.png')
cookie = pygame.transform.scale(cookie, (120, 120))
hitbox = cookie.get_rect()

# Устанавливаем случайное начальное положение и направление движения
hitbox.x = random.choice([0, w])  # Начальная позиция по горизонтали (лево или право)
hitbox.y = random.randint(0, h - hitbox.height)  # Начальная позиция по вертикали (от верхнего края до нижнего)
speed = random.choice([-5, 5])  # Случайное направление движения (влево или вправо)

score = 0

font = pygame.font.Font(None, 48)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hitbox.x += speed

    # Проверяем, достигла ли картинка края экрана
    if hitbox.left > w or hitbox.right < 0:
        hitbox.x = random.choice([0, w])  # Появляем картинку с противоположной стороны
        hitbox.y = random.randint(0, h - hitbox.height)  # Выбираем случайную высоту на экране
        speed *= -1  # Меняем направление движения на противоположное

    screen.fill((0, 200, 200))

    text = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    screen.blit(cookie, hitbox)
    pygame.display.update()

pygame.quit()

