import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Устанавливаем размер окна
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Попади в печеньку')
speed = 6
speed_x = speed
speed_y = speed

# Загружаем и масштабируем изображение cookie.png
cookie_image = pygame.image.load('cookie.png')
cookie_image = pygame.transform.scale(cookie_image, (120, 120))

# Устанавливаем начальные координаты в центре экрана и скорость движения cookie
cookie_x, cookie_y = window_size[0] // 2 - cookie_image.get_width() // 2, window_size[1] // 2 - cookie_image.get_height() // 2
cookie_speed_x, cookie_speed_y = speed_x, speed_y

# Устанавливаем начальный счет
score = 0
lastScore = 10

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        # Проверяем клик мышью на картинку cookie
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (cookie_x <= mouse_x <= cookie_x + cookie_image.get_width()
                    and cookie_y <= mouse_y <= cookie_y + cookie_image.get_height()):
                score += 1
                if score == lastScore:
                    lastScore += 10
                    speed += 1
                print(f'Score: {score}')
                print(f'Speed: {speed}')

    # Двигаем cookie и проверяем, достигла ли она края окна
    cookie_x += cookie_speed_x
    cookie_y += cookie_speed_y

    if cookie_x < 0:
        cookie_x = 0
        cookie_speed_x *= -1
    elif cookie_x > window_size[0] - cookie_image.get_width():
        cookie_x = window_size[0] - cookie_image.get_width()
        cookie_speed_x *= -1

    if cookie_y < 0:
        cookie_y = 0
        cookie_speed_y *= -1
    elif cookie_y > window_size[1] - cookie_image.get_height():
        cookie_y = window_size[1] - cookie_image.get_height()
        cookie_speed_y *= -1

    # Отрисовываем cookie и счет на экране
    window.fill((69, 15, 247))  # Заливаем фон синим цветом
    window.blit(cookie_image, (cookie_x, cookie_y))  # Рисуем cookie
    font = pygame.font.Font(None, 36)
    text = font.render(f'Счёт: {score}', True, (15, 247, 100))  # зелёный
    textSpeed = font.render(f'Скорость: {speed}', True, (247, 54, 15))  # красный
    window.blit(text, (20, 20))  # Рисуем счет
    window.blit(textSpeed, (20, 50))  # Рисуем скорость

    pygame.display.flip()  # Обновляем экран

    # Задаем частоту обновления кадров
    pygame.time.Clock().tick(60)
