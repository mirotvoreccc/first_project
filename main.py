def first_func():
    import pygame
    import time

    pygame.init()

    window_width = 800
    window_height = 600
    fon = 'windows-10-red.jpg'

    # Запуск
    window = pygame.display.set_mode([window_width, window_height])  # создание окна указанных размеров
    pygame.display.set_caption("Игра v1.0")  # установка надписи окна программы

    speed = 0  # текущая скорость перемещения
    sdvig_fona = 0

    try:
        img1 = pygame.image.load(fon)  # загрузка фона игры из файла
        back_fon = pygame.transform.scale(img1, (window_width, window_height))
    except:
        # Если изображение не найдено, создаем простой фон
        back_fon = pygame.Surface((window_width, window_height))
        back_fon.fill((100, 150, 200))  # Цвет фона
        # Добавляем простой узор для визуализации движения
        for x in range(0, window_width, 50):
            for y in range(0, window_height, 50):
                pygame.draw.circle(back_fon, (255, 255, 255), (x, y), 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # пришло ли событие нажатия на крестик
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = -5  # Отрицательная скорость для движения влево
                elif event.key == pygame.K_RIGHT:
                    speed = 5  # Положительная скорость для движения вправо
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    speed = 0  # Остановка при отпускании клавиши

        sdvig_fona = (sdvig_fona + speed) % window_width

        # Отрисовка фона
        window.blit(back_fon, (sdvig_fona, 0))
        if sdvig_fona != 0:
            window.blit(back_fon, (sdvig_fona - window_width, 0))
        else:
            window.blit(back_fon, (sdvig_fona + window_width, 0))

        pygame.display.update()  # обновилось содержимое окна
        time.sleep(0.02)

    pygame.quit()  # закрыть окно крестиком


def second_func():
    import pygame



    pygame.init()


    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Аркада с движущимся фоном")

    # Класс игрока
    class Player(pygame.sprite.Sprite):
        def __init__(self, filename, hero_x=100, hero_y=250, x_speed=0, y_speed=0):
            pygame.sprite.Sprite.__init__(self)
            original_image = pygame.image.load(filename)  # загрузка изображения персонажа

            self.image = pygame.transform.scale(original_image, (100, 200))
            self.rect = self.image.get_rect()
            self.hero_x = hero_x
            self.hero_y = hero_y
            self.rect.x = hero_x  # начальная позиция по X
            self.rect.y = hero_y  # начальная позиция по Y
            self.x_speed = x_speed  # скорость по горизонтали
            self.y_speed = y_speed  # скорость по вертикали
            self.screen_width = WINDOW_WIDTH
            self.screen_height = WINDOW_HEIGHT

        def update(self):
            """Перемещает персонажа с учетом текущей скорости"""
            # Обновляем позицию
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed

            # Ограничиваем движение в пределах экрана
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.screen_width:
                self.rect.right = self.screen_width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > self.screen_height:
                self.rect.bottom = self.screen_height

    # Загрузка фона
    try:
        background = pygame.image.load('windows-10-red.jpg')
        background = pygame.transform.scale(background, (WINDOW_WIDTH * 2, WINDOW_HEIGHT))
    except:
        # Создаем простой фон, если изображение не найдено
        background = pygame.Surface((WINDOW_WIDTH * 2, WINDOW_HEIGHT))
        background.fill((50, 100, 150))
        for x in range(0, WINDOW_WIDTH * 2, 50):
            for y in range(0, WINDOW_HEIGHT, 50):
                pygame.draw.circle(background, (200, 200, 200), (x, y), 5)

    # Создание игрока
    try:
        player = Player('fanta.jpg')
    except:
        # Создаем простого игрока, если изображение не найдено
        player_surface = pygame.Surface((50, 80))
        player_surface.fill((255, 0, 0))
        pygame.draw.rect(player_surface, (0, 255, 0), (10, 10, 30, 60))
        player = Player(player_surface, 100, 250)

    # Параметры фона
    bg_x = 0  # Позиция фона по X
    bg_speed = 0  # Скорость движения фона
    player_speed = 5  # Скорость игрока

    # Группа спрайтов
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Основной игровой цикл
    clock = pygame.time.Clock()
    running = True

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_speed = -player_speed
                elif event.key == pygame.K_RIGHT:
                    player.x_speed = player_speed
                elif event.key == pygame.K_UP:
                    player.y_speed = -player_speed
                elif event.key == pygame.K_DOWN:
                    player.y_speed = player_speed

            # Обработка отпускания клавиш
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.y_speed = 0

        # Обновление спрайтов
        all_sprites.update()

        # Движение фона при достижении границ
        if player.rect.right >= WINDOW_WIDTH - 50 and player.x_speed > 0:
            bg_x -= player_speed
            player.rect.x -= player_speed
        elif player.rect.left <= 50 and player.x_speed < 0 and bg_x < 0:
            bg_x += player_speed
            player.rect.x += player_speed

        # Ограничение движения фона
        bg_x = max(-WINDOW_WIDTH, min(bg_x, 0))

        # Отрисовка
        window.fill((0, 0, 0))  # Черный фон на случай, если изображение меньше окна
        window.blit(background, (bg_x, 0))  # Рисуем фон с учетом смещения
        all_sprites.draw(window)  # Рисуем все спрайты

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()



def third_func():
    import pygame
    import random

    # Инициализация Pygame
    pygame.init()

    # Настройки окна
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Аркада с коллизиями")

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Класс игрока
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y, color=GREEN):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speed = 5

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed

            # Ограничение движения в пределах экрана
            self.rect.x = max(0, min(self.rect.x, WINDOW_WIDTH - self.rect.width))
            self.rect.y = max(0, min(self.rect.y, WINDOW_HEIGHT - self.rect.height))

    # Класс врага
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30, 30))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randrange(WINDOW_HEIGHT - self.rect.height)
            self.speed_x = random.randrange(-3, 3)
            self.speed_y = random.randrange(-3, 3)

        def update(self):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            # Отскок от краев
            if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
                self.speed_x *= -1
            if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
                self.speed_y *= -1

    # Класс стрелы
    class Arrow(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((20, 10))
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speed = 10
            self.lifetime = 60  # Время жизни в кадрах

        def update(self):
            self.rect.x += self.speed
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.kill()  # Удаляем стрелу, если время жизни истекло

    # Создание групп спрайтов
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    arrows = pygame.sprite.Group()

    # Создание игрока
    player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    all_sprites.add(player)

    # Создание врагов
    for i in range(5):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Основной игровой цикл
    clock = pygame.time.Clock()
    running = True

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Создание стрелы при нажатии пробела
                    arrow = Arrow(player.rect.right, player.rect.centery)
                    all_sprites.add(arrow)
                    arrows.add(arrow)

        # Обновление спрайтов
        all_sprites.update()

        # Проверка коллизий стрел с врагами
        hits = pygame.sprite.groupcollide(arrows, enemies, True, True)

        # Если нужно создать новых врагов при уничтожении всех
        if len(enemies) == 0:
            for i in range(5):
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

        # Отрисовка
        window.fill(BLACK)
        all_sprites.draw(window)
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

#first_func()
#second_func()
#third_func()