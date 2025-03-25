def first_ex():
    import pygame
    import random


    pygame.init()

    # 1. Создание окна 800x600 с возможностью растягивания
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Таранник Иван")

    # 2. Белый фон
    screen.fill((255, 255, 255))

    # 10. Загрузка и отображение изображения
    try:
        image = pygame.image.load("minion.jpg")
        screen.blit(image, [300, 200])
    except:
        print("Изображение не найдено")

    # Обновление экрана
    pygame.display.flip()

    pygame.time.delay(2000)
    # 11. Перемещение изображения

    new_x, new_y = 100, 200
    screen.fill((255, 255, 255))  # Очистка экрана
    screen.blit(image, (new_x, new_y))
    pygame.display.flip()

    pygame.time.delay(2000)

    # 3. Закрашенный красный круг (1-я четверть)
    pygame.draw.circle(screen, (255, 0, 0), (600, 150), 50)

    # 4. Круг с контуром (ширина=15)
    pygame.draw.circle(screen, 'red', [600, 450], 70, width= 15)

    # 5. Круг в центре экрана (радиус=100)
    center_x, center_y = screen.get_width() // 2, screen.get_height() // 2
    pygame.draw.circle(screen, 'orange', (center_x, center_y), 100)

    # 6. Прямоугольник 300x200 (закрашенный)
    pygame.draw.rect(screen, 'blue', (450, 350, 300, 200))

    # 7. Пять случайных прямоугольников
    for _ in range(5):
        x = random.randint(0, 700)
        y = random.randint(0, 500)
        width = random.randint(50, 150)
        height = random.randint(50, 150)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(screen, color, (x, y, width, height))

    # 8. Домик из линий
    # Основание
    pygame.draw.polygon(screen, (139, 69, 19), [(100, 400), (300, 400), (300, 200), (100, 200)])
    # Крыша
    pygame.draw.polygon(screen, (255, 0, 0), [(80, 200), (200, 100), (320, 200)])

    # 9. Произвольная фигура (звезда)
    points = [
        (400, 100), (430, 180), (520, 180),
        (450, 220), (480, 300), (400, 250),
        (320, 300), (350, 220), (280, 180),
        (370, 180)
    ]
    pygame.draw.polygon(screen, (255, 255, 0), points)



    # Основной цикл (чтобы окно не закрывалось сразу)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()


def second_ex():
    import pygame
    import random


    # Инициализация Pygame
    pygame.init()

    # Настройки окна
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Анимация фигур")

    # Цвета
    WHITE = (255, 255, 255)

    # Параметры фигур
    shapes = [
        {"type": "rect", "x": 100, "y": 100, "width": 100, "height": 80,
         "color": (255, 0, 0), "speed_x": 3, "speed_y": 0},
        {"type": "circle", "x": 300, "y": 300, "radius": 40,
         "color": (0, 255, 0), "speed_x": 0, "speed_y": 4},
        {"type": "triangle", "x": 500, "y": 200, "size": 60,
         "color": (0, 0, 255), "speed_x": 2, "speed_y": 2}
    ]

    # Основной цикл
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Обработка клика мышью
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for shape in shapes:
                    if shape["type"] == "rect":
                        if (shape["x"] <= mouse_pos[0] <= shape["x"] + shape["width"] and
                                shape["y"] <= mouse_pos[1] <= shape["y"] + shape["height"]):
                            shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    elif shape["type"] == "circle":
                        distance = ((mouse_pos[0] - shape["x"]) ** 2 + (mouse_pos[1] - shape["y"]) ** 2) ** 0.5
                        if distance <= shape["radius"]:
                            shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    elif shape["type"] == "triangle":
                        # Упрощенная проверка для треугольника (прямоугольная область)
                        if (shape["x"] <= mouse_pos[0] <= shape["x"] + shape["size"] and
                                shape["y"] <= mouse_pos[1] <= shape["y"] + shape["size"]):
                            shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Движение и отрисовка фигур
        for shape in shapes:
            # Движение
            shape["x"] += shape["speed_x"]
            shape["y"] += shape["speed_y"]

            # Отскок от границ
            if shape["type"] == "rect":
                if shape["x"] <= 0 or shape["x"] + shape["width"] >= WIDTH:
                    shape["speed_x"] *= -1
                    shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if shape["y"] <= 0 or shape["y"] + shape["height"] >= HEIGHT:
                    shape["speed_y"] *= -1
                    shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            elif shape["type"] == "circle":
                if shape["x"] - shape["radius"] <= 0 or shape["x"] + shape["radius"] >= WIDTH:
                    shape["speed_x"] *= -1
                    shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if shape["y"] - shape["radius"] <= 0 or shape["y"] + shape["radius"] >= HEIGHT:
                    shape["speed_y"] *= -1
                    shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            elif shape["type"] == "triangle":
                if shape["x"] <= 0 or shape["x"] + shape["size"] >= WIDTH:
                    shape["speed_x"] *= -1
                    shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if shape["y"] <= 0 or shape["y"] + shape["size"] >= HEIGHT:
                    shape["speed_y"] *= -1
                    shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Отрисовка
            if shape["type"] == "rect":
                pygame.draw.rect(screen, shape["color"], (shape["x"], shape["y"], shape["width"], shape["height"]))

            elif shape["type"] == "circle":
                pygame.draw.circle(screen, shape["color"], (int(shape["x"]), int(shape["y"])), shape["radius"])

            elif shape["type"] == "triangle":
                points = [
                    (shape["x"], shape["y"] + shape["size"]),
                    (shape["x"] + shape["size"] // 2, shape["y"]),
                    (shape["x"] + shape["size"], shape["y"] + shape["size"])
                ]
                pygame.draw.polygon(screen, shape["color"], points)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



#first_ex()
second_ex()