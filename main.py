import pygame

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BROWN = (205, 127, 50)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
DARK_GREEN = (50, 205, 50)
PINK = (255, 20, 147)
BEIGE = (248, 131, 121)
TURQUOISE = (19, 84, 78)

WIDTH, HEIGHT = 650, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 140

RECTANGLE_PLAYER_WIDTH = 40
RECTANGLE_PLAYER_HEIGHT = 40
RECTANGLE_SPEED = 1

#HUVUDMENY
if True:
    CIRCLE_RADIUS = 23
    CIRCLE_COLOR = (255, 255, 255)
    CIRCLE_SPEED = 1

    RECTANGLE_WIDTH = 100
    RECTANGLE_HEIGHT = 100
    RECTANGLE_POS_X = [50, 200, 350, 500]
    RECTANGLE_POS_Y = [50, 50, 50, 50]

    TEXT_SIZE = 90
    NUMBER_SIZE = 100
    INFO_FONT = pygame.font.SysFont("Ariel", TEXT_SIZE)
    NUMBER_FONT = pygame.font.SysFont("Ariel", NUMBER_SIZE)
    ENTER_TEXT = INFO_FONT.render("SPACE T     ENTER", 1, WHITE)
    EXIT_TEXT = INFO_FONT.render("BACKSPACE TO EXIT", 1, WHITE)
    BACK_TEXT = INFO_FONT.render("TAB TO RETURN", 1, WHITE)

    NUMBER_1 = NUMBER_FONT.render("1", 1, BLACK)
    NUMBER_2 = NUMBER_FONT.render("2", 1, BLACK)
    NUMBER_3 = NUMBER_FONT.render("3", 1, BLACK)
    NUMBER_4 = NUMBER_FONT.render("4", 1, BLACK)
    NUMBER_Y = 70

    START_POS_X_HUVUDMENY = WIDTH/2 - 30
    START_POS_Y_HUVUDMENY = 347

    def clamp(rectangle_x, rectangle_y, circle_x, circle_y, level):
        if level == "Huvudmeny":
            if circle_x < rectangle_x:
                x_value = rectangle_x
            elif circle_x > rectangle_x + RECTANGLE_WIDTH:
                x_value = rectangle_x + RECTANGLE_WIDTH
            else:
                x_value = circle_x

            if circle_y < rectangle_y:
                y_value = rectangle_y
            elif circle_y > rectangle_y + RECTANGLE_HEIGHT:
                y_value = rectangle_y + RECTANGLE_HEIGHT
            else:
                y_value = circle_y

            value = (x_value, y_value)

            return value

#LEVEL 1
if True:
    COLLISION_TOLERANCE = 5

    RECTANGLE_PLAYER_X_1= WIDTH/2 - RECTANGLE_PLAYER_WIDTH/2
    RECTANGLE_PLAYER_Y_1= 540

    RECTANGLE_WIDTH_1 = 20
    RECTANGLE_HEIGHT_1 = 20
    RECTANGLE_COLOR_UNPRESSED = (255, 0, 0)
    RECTANGLE_COLOR_PRESSED = (0, 255, 0)
    RED_GREEN_COLOR_1, RED_GREEN_COLOR_2, RED_GREEN_COLOR_3, RED_GREEN_COLOR_4, RED_GREEN_COLOR_5 = RECTANGLE_COLOR_UNPRESSED, RECTANGLE_COLOR_UNPRESSED, RECTANGLE_COLOR_UNPRESSED, RECTANGLE_COLOR_UNPRESSED, RECTANGLE_COLOR_UNPRESSED
    RED_GREEN_COLOR = [RED_GREEN_COLOR_1, RED_GREEN_COLOR_2, RED_GREEN_COLOR_3, RED_GREEN_COLOR_4, RED_GREEN_COLOR_5]
    RECTANGLE_POS_X_1 = [30, 30, WIDTH/2-RECTANGLE_WIDTH_1/2, 600, 600]
    RECTANGLE_POS_Y_1 = [30, 550, HEIGHT/2-RECTANGLE_HEIGHT_1/2, 30, 550]


    RED_GREEN = [
        pygame.Rect(RECTANGLE_POS_X_1[0], RECTANGLE_POS_Y_1[0], RECTANGLE_WIDTH_1, RECTANGLE_HEIGHT_1),
        pygame.Rect(RECTANGLE_POS_X_1[1], RECTANGLE_POS_Y_1[1], RECTANGLE_WIDTH_1, RECTANGLE_HEIGHT_1),
        pygame.Rect(RECTANGLE_POS_X_1[2], RECTANGLE_POS_Y_1[2], RECTANGLE_WIDTH_1, RECTANGLE_HEIGHT_1),
        pygame.Rect(RECTANGLE_POS_X_1[3], RECTANGLE_POS_Y_1[3], RECTANGLE_WIDTH_1, RECTANGLE_HEIGHT_1),
        pygame.Rect(RECTANGLE_POS_X_1[4], RECTANGLE_POS_Y_1[4], RECTANGLE_WIDTH_1, RECTANGLE_HEIGHT_1)
    ]
    WALL_COLOR = WHITE

    SPACE = 69
    WALL_WIDTH = 5

    HORIZONTAL_LENGTH = 215
    HORIZONTAL_LEFT = SPACE
    HORIZONTAL_RIGHT = WIDTH - SPACE - HORIZONTAL_LENGTH

    VERTICAL_LENGTH = HORIZONTAL_LENGTH - WALL_WIDTH - 25
    VERTICAL_UP = SPACE + WALL_WIDTH
    VERTICAL_DOWN = HEIGHT - SPACE - WALL_WIDTH - VERTICAL_LENGTH

    WALLS1 = [
        # Horizontal
        pygame.Rect(HORIZONTAL_LEFT, SPACE, HORIZONTAL_LENGTH, WALL_WIDTH),
        pygame.Rect(HORIZONTAL_RIGHT, SPACE, HORIZONTAL_LENGTH, WALL_WIDTH),

        pygame.Rect(HORIZONTAL_LEFT, HEIGHT - SPACE - WALL_WIDTH, HORIZONTAL_LENGTH, WALL_WIDTH),
        pygame.Rect(HORIZONTAL_RIGHT, HEIGHT - SPACE - WALL_WIDTH, HORIZONTAL_LENGTH, WALL_WIDTH),

        # Vertical
        pygame.Rect(HORIZONTAL_LEFT, VERTICAL_UP, WALL_WIDTH, VERTICAL_LENGTH),
        pygame.Rect(WIDTH - SPACE - WALL_WIDTH, VERTICAL_UP, WALL_WIDTH, VERTICAL_LENGTH),

        pygame.Rect(HORIZONTAL_LEFT, VERTICAL_DOWN, WALL_WIDTH, VERTICAL_LENGTH),
        pygame.Rect(WIDTH - SPACE - WALL_WIDTH, VERTICAL_DOWN, WALL_WIDTH, VERTICAL_LENGTH),
    ]

    def red_green():
        i = 0
        for box in RED_GREEN:
            pygame.draw.rect(WIN, RED_GREEN_COLOR[i], box)
            i += 1

    def walls1():
        for wall in WALLS1:
            pygame.draw.rect(WIN, WALL_COLOR, wall)

#LEVEL 2
if True:
    GOAL = 500, 0, 150, 180

    RECTANGLE_PLAYER_X_2 = 10
    RECTANGLE_PLAYER_Y_2 = HEIGHT/2 - RECTANGLE_PLAYER_HEIGHT/2

    BOX_POS_X = 270
    BOX_POS_Y = 70
    BOX_WIDTH_2 = 80
    BOX_HEIGHT_2 = 120

    GROW_BUTTON = 500, 350, 20, 20
    SHRINK_BUTTON = 500, 450, 20, 20

    BOX_STOP_WIDTH = 30
    BOX_STOP_HEIGHT = 10

    BOX_STOP_1_X = 270
    BOX_STOP_1_Y = 60
    BOX_STOP_2_X = 270
    BOX_STOP_2_Y = 300

    box = pygame.Rect(BOX_POS_X, BOX_POS_Y, BOX_WIDTH_2, BOX_HEIGHT_2)
    box_stop_1 = pygame.Rect(BOX_STOP_1_X, BOX_STOP_1_Y, BOX_STOP_WIDTH, BOX_STOP_HEIGHT)
    box_stop_2 = pygame.Rect(BOX_STOP_2_X, BOX_STOP_2_Y, BOX_STOP_WIDTH, BOX_STOP_HEIGHT)

    goal = pygame.Rect(GOAL)

    grow_button = pygame.Rect(GROW_BUTTON)
    shrink_button = pygame.Rect(SHRINK_BUTTON)

    WALLS2 = [
        pygame.Rect(350, 0, 10, 150),
        pygame.Rect(350, 300, 10, 300),

        pygame.Rect(350, 180, 300, 10),
    ]

    def walls2():
        for wall in WALLS2:
            pygame.draw.rect(WIN, WALL_COLOR, wall)

#LEVEL 3
if True:
    RECTANGLE_PLAYER_X_3 = 20
    RECTANGLE_PLAYER_Y_3 = 400

    BOX_WIDTH_3 = 90
    BOX_HEIGHT_3 = 155
    BOX_POS_X_3 = 200
    BOX_POS_Y_3 = 55

    TIMER = 10000
    timer_start = 100000000

    box_3 = pygame.Rect(BOX_POS_X_3, BOX_POS_Y_3, BOX_WIDTH_3, BOX_HEIGHT_3)

    GOAL_3 = 0, 5, 50, 195
    goal_3 = pygame.Rect(GOAL_3)

    GROW_BUTTON_3 = 195, 400, 20, 20
    SHRINK_BUTTON_3 = 585, 50, 20, 20

    grow_button_3 = pygame.Rect(GROW_BUTTON_3)
    shrink_button_3 = pygame.Rect(SHRINK_BUTTON_3)

    WALLS3 = [
        pygame.Rect(0, 200, 200, 10),
        pygame.Rect(290, 0, 10, 210),

        pygame.Rect(410, 200, 10, 400),
        pygame.Rect(530, 0, 10, 400),

        pygame.Rect(50, 0, 10, 175)
    ]

    def walls3():
        for wall in WALLS3:
            pygame.draw.rect(WIN, WALL_COLOR, wall)

    def timer(current_time, timer_start):
        if current_time - timer_start > TIMER and box_3.y < BOX_POS_Y_3:
            box_3.y += 1
        if box_3.y == BOX_POS_Y_3:
            timer_start = 10000000

        return timer_start

#LEVEL 4
if True:
    RECTANGLE_PLAYER_X_4 = 20
    RECTANGLE_PLAYER_Y_4 = 350
    PLAYER_COLOR = WHITE

    GOAL_4 = 385, 350, 265, 100
    goal_4 = pygame.Rect(GOAL_4)

    RED_CHANGE = pygame.Rect(0, 550, 163, 50)
    ORANGE_CHANGE = pygame.Rect(163, 550, 162, 50)
    PURPLE_CHANGE = pygame.Rect(325, 550, 162, 50)
    BROWN_CHANGE = pygame.Rect(487, 550, 163, 50)

    DARK_GREEN_CHANGE = pygame.Rect(0, 0, 50, 100)
    TURQUOISE_CHANGE = pygame.Rect(0, 100, 50, 100)
    PINK_CHANGE = pygame.Rect(325, 0, 50, 100)
    BEIGE_CHANGE = pygame.Rect(325, 100, 50, 100)

    BLUE_CHANGE = pygame.Rect(575, 0, 75, 75)

    WALLS4 = [
        pygame.Rect(375, 450, 275, 10),

        pygame.Rect(375, 0, 10, 200),

        pygame.Rect(375, 300, 10, 150),
    ]
    BLUE_WALLS = [
        pygame.Rect(385, 300, 265, 10),
        pygame.Rect(510, 140, 140, 10)
    ]
    YELLOW_WALLS = [
        pygame.Rect(500, 0, 10, 150)
    ]

    def walls4():
        for wall in WALLS4:
            pygame.draw.rect(WIN, WALL_COLOR, wall)

    def blue_walls():
        for wall in BLUE_WALLS:
            pygame.draw.rect(WIN, BLUE, wall)

    def yellow_walls():
        for wall in YELLOW_WALLS:
            pygame.draw.rect(WIN, YELLOW, wall)

    def wall_collision_4(wall, rectangle_player):
        if abs(wall.top - rectangle_player.bottom) < COLLISION_TOLERANCE:
            rectangle_player.y -= RECTANGLE_SPEED
        if abs(wall.bottom - rectangle_player.top) < COLLISION_TOLERANCE:
            rectangle_player.y += RECTANGLE_SPEED
        if abs(wall.left - rectangle_player.right) < COLLISION_TOLERANCE:
            rectangle_player.x -= RECTANGLE_SPEED
        if abs(wall.right - rectangle_player.left) < COLLISION_TOLERANCE:
            rectangle_player.x += RECTANGLE_SPEED


def window(level, circle_x, circle_y, rectangle_player, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, PLAYER_COLOR):
    pygame.display.set_caption(level)
    if level == "Huvudmeny":
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, YELLOW, (RECTANGLE_POS_X[0], RECTANGLE_POS_Y[0], RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
        pygame.draw.rect(WIN, GREEN, (RECTANGLE_POS_X[1], RECTANGLE_POS_Y[1], RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
        pygame.draw.rect(WIN, BLUE, (RECTANGLE_POS_X[2], RECTANGLE_POS_Y[2], RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
        pygame.draw.rect(WIN, RED, (RECTANGLE_POS_X[3], RECTANGLE_POS_Y[3], RECTANGLE_WIDTH, RECTANGLE_HEIGHT))

        WIN.blit(ENTER_TEXT, (0, 320))
        WIN.blit(BACK_TEXT, (0, 420))
        WIN.blit(EXIT_TEXT, (0, 520))

        WIN.blit(NUMBER_1, (80, NUMBER_Y))
        WIN.blit(NUMBER_2, (230, NUMBER_Y))
        WIN.blit(NUMBER_3, (380, NUMBER_Y))
        WIN.blit(NUMBER_4, (530, NUMBER_Y))

        pygame.draw.circle(WIN, CIRCLE_COLOR, (circle_x, circle_y), CIRCLE_RADIUS)

    elif level == "Level 1":
        pygame.draw.rect(WIN, WHITE, (rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT))
        red_green()
        walls1()
    elif level == "Level 2":
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, WHITE, (rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT))
        pygame.draw.rect(WIN, WHITE, (box.x, box.y, BOX_WIDTH_2, BOX_HEIGHT_2))

        pygame.draw.rect(WIN, WHITE, (box_stop_1.x, box_stop_1.y, BOX_STOP_WIDTH, BOX_STOP_HEIGHT))
        pygame.draw.rect(WIN, WHITE, (box_stop_2.x, box_stop_2.y, BOX_STOP_WIDTH, BOX_STOP_HEIGHT))

        pygame.draw.rect(WIN, GREEN, (GOAL))

        pygame.draw.rect(WIN, BLUE, (GROW_BUTTON))
        pygame.draw.rect(WIN, RED, (SHRINK_BUTTON))

        walls2()
    elif level == "Level 3":
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, WHITE, (rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT))
        pygame.draw.rect(WIN, WHITE, (box_3.x, box_3.y, BOX_WIDTH_3, BOX_HEIGHT_3))
        pygame.draw.rect(WIN, WHITE, (0, 0, 650, 5))

        pygame.draw.rect(WIN, GREEN, (GOAL_3))
        pygame.draw.rect(WIN, BLUE, (GROW_BUTTON_3))
        pygame.draw.rect(WIN, RED, (SHRINK_BUTTON_3))

        walls3()
    elif level == "Level 4":
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, PLAYER_COLOR, (rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT))
        pygame.draw.rect(WIN, GREEN, (GOAL_4))

        pygame.draw.rect(WIN, RED, (RED_CHANGE))
        pygame.draw.rect(WIN, ORANGE, (ORANGE_CHANGE))
        pygame.draw.rect(WIN, PURPLE, (PURPLE_CHANGE))
        pygame.draw.rect(WIN, BROWN, (BROWN_CHANGE))

        pygame.draw.rect(WIN, DARK_GREEN, (DARK_GREEN_CHANGE))
        pygame.draw.rect(WIN, TURQUOISE, (TURQUOISE_CHANGE))
        pygame.draw.rect(WIN, PINK, (PINK_CHANGE))
        pygame.draw.rect(WIN, BEIGE, (BEIGE_CHANGE))

        pygame.draw.rect(WIN, BLUE, (BLUE_CHANGE))


        walls4()
        blue_walls()
        yellow_walls()

    pygame.display.update()


def movement(keys_pressed, circle_x, circle_y, level, rectangle_player, trail, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT):
    if level == "Huvudmeny":
        if keys_pressed[pygame.K_w] and (circle_y - CIRCLE_RADIUS - CIRCLE_SPEED) > 0: # UP
            circle_y -= CIRCLE_SPEED
        if keys_pressed[pygame.K_s] and (circle_y + CIRCLE_RADIUS + CIRCLE_SPEED) < HEIGHT: # DOWN
            circle_y += CIRCLE_SPEED
        if keys_pressed[pygame.K_d] and (circle_x + CIRCLE_RADIUS + CIRCLE_SPEED) < WIDTH:  # RIGHT
            circle_x += CIRCLE_SPEED
        if keys_pressed[pygame.K_a] and (circle_x - CIRCLE_RADIUS - CIRCLE_SPEED) > 0:  # LEFT
            circle_x -= CIRCLE_SPEED

    if level == "Level 1":
        if keys_pressed[pygame.K_w] and (rectangle_player.y - RECTANGLE_SPEED) > 0:  # UP
            rectangle_player.y -= RECTANGLE_SPEED
            trail.append(pygame.Rect(rectangle_player.x, rectangle_player.y+RECTANGLE_PLAYER_HEIGHT+1, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))
            pygame.draw.rect(WIN, RED, (rectangle_player.x, rectangle_player.y+RECTANGLE_PLAYER_HEIGHT, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))

        if keys_pressed[pygame.K_s] and (rectangle_player.y + RECTANGLE_PLAYER_HEIGHT + RECTANGLE_SPEED) < HEIGHT:  # DOWN
            rectangle_player.y += RECTANGLE_SPEED
            trail.append(pygame.Rect(rectangle_player.x, rectangle_player.y-RECTANGLE_SPEED-1, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))
            pygame.draw.rect(WIN, RED, (rectangle_player.x, rectangle_player.y-RECTANGLE_SPEED, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))

        if keys_pressed[pygame.K_d] and (rectangle_player.x + RECTANGLE_SPEED + RECTANGLE_PLAYER_WIDTH) < WIDTH:  # RIGHT
            rectangle_player.x += RECTANGLE_SPEED
            trail.append(pygame.Rect(rectangle_player.x-RECTANGLE_SPEED-1, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))
            pygame.draw.rect(WIN, RED, (rectangle_player.x-RECTANGLE_SPEED, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))

        if keys_pressed[pygame.K_a] and (rectangle_player.x - RECTANGLE_SPEED) > 0:  # LEFT
            rectangle_player.x -= RECTANGLE_SPEED
            trail.append(pygame.Rect(rectangle_player.x+RECTANGLE_PLAYER_WIDTH+1, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))
            pygame.draw.rect(WIN, RED, (rectangle_player.x+RECTANGLE_PLAYER_WIDTH, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))

    if level == "Level 2":
        if keys_pressed[pygame.K_w] and (rectangle_player.y - RECTANGLE_SPEED) > 0:  # UP
            rectangle_player.y -= RECTANGLE_SPEED
        if keys_pressed[pygame.K_s] and (rectangle_player.y + RECTANGLE_PLAYER_HEIGHT + RECTANGLE_SPEED) < HEIGHT:  # DOWN
            rectangle_player.y += RECTANGLE_SPEED
        if keys_pressed[pygame.K_d] and (rectangle_player.x + RECTANGLE_SPEED + RECTANGLE_PLAYER_WIDTH) < WIDTH:  # RIGHT
            rectangle_player.x += RECTANGLE_SPEED
        if keys_pressed[pygame.K_a] and (rectangle_player.x - RECTANGLE_SPEED) > 0:  # LEFT
            rectangle_player.x -= RECTANGLE_SPEED

    if level == "Level 3":
        if keys_pressed[pygame.K_w] and (rectangle_player.y - RECTANGLE_SPEED) > 0:  # UP
            rectangle_player.y -= RECTANGLE_SPEED
        if keys_pressed[pygame.K_s] and (rectangle_player.y + RECTANGLE_PLAYER_HEIGHT + RECTANGLE_SPEED) < HEIGHT:  # DOWN
            rectangle_player.y += RECTANGLE_SPEED
        if keys_pressed[pygame.K_d] and (rectangle_player.x + RECTANGLE_SPEED + RECTANGLE_PLAYER_WIDTH) < WIDTH:  # RIGHT
            rectangle_player.x += RECTANGLE_SPEED
        if keys_pressed[pygame.K_a] and (rectangle_player.x - RECTANGLE_SPEED) > 0:  # LEFT
            rectangle_player.x -= RECTANGLE_SPEED

    if level == "Level 4":
        if keys_pressed[pygame.K_w] and (rectangle_player.y - RECTANGLE_SPEED) > 0:  # UP
            rectangle_player.y -= RECTANGLE_SPEED
        if keys_pressed[pygame.K_s] and (rectangle_player.y + RECTANGLE_PLAYER_HEIGHT + RECTANGLE_SPEED) < HEIGHT:  # DOWN
            rectangle_player.y += RECTANGLE_SPEED
        if keys_pressed[pygame.K_d] and (rectangle_player.x + RECTANGLE_SPEED + RECTANGLE_PLAYER_WIDTH) < WIDTH:  # RIGHT
            rectangle_player.x += RECTANGLE_SPEED
        if keys_pressed[pygame.K_a] and (rectangle_player.x - RECTANGLE_SPEED) > 0:  # LEFT
            rectangle_player.x -= RECTANGLE_SPEED

    return circle_x, circle_y, rectangle_player, trail

def collision(circle_x, circle_y, keys_pressed, level, rectangle_player, RED_GREEN_COLOR, trail, KOD, box, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, current_time, timer_start, PLAYER_COLOR):
    if level == "Huvudmeny":
        for i in range(len(RECTANGLE_POS_X)):
            rectangle_x = RECTANGLE_POS_X[i]
            rectangle_y = RECTANGLE_POS_Y[i]
            value = clamp(rectangle_x, rectangle_y, circle_x, circle_y, level)
            if value == (circle_x, circle_y):
                HOWER = True
            else:
                HOWER = False
            if HOWER and keys_pressed[pygame.K_SPACE] and circle_x < RECTANGLE_POS_X[0] + RECTANGLE_WIDTH:
                level = "Level 1"
                WIN.fill(BLACK)
                rectangle_player.x = RECTANGLE_PLAYER_X_1
                rectangle_player.y = RECTANGLE_PLAYER_Y_1
                RECTANGLE_PLAYER_WIDTH = 40
                RECTANGLE_PLAYER_HEIGHT = 40

            elif HOWER and keys_pressed[pygame.K_SPACE] and circle_x < RECTANGLE_POS_X[1] + RECTANGLE_WIDTH:
                level = "Level 2"
                rectangle_player.x = RECTANGLE_PLAYER_X_2
                rectangle_player.y = RECTANGLE_PLAYER_Y_2
                RECTANGLE_PLAYER_WIDTH = 40
                RECTANGLE_PLAYER_HEIGHT = 40
                box.x = BOX_POS_X
                box.y = BOX_POS_Y

            elif HOWER and keys_pressed[pygame.K_SPACE] and circle_x < RECTANGLE_POS_X[2] + RECTANGLE_WIDTH:
                level = "Level 3"
                rectangle_player.x = RECTANGLE_PLAYER_X_3
                rectangle_player.y = RECTANGLE_PLAYER_Y_3
                RECTANGLE_PLAYER_WIDTH = 40
                RECTANGLE_PLAYER_HEIGHT = 40
                box_3.x = BOX_POS_X_3
                box_3.y = BOX_POS_Y_3


            elif HOWER and keys_pressed[pygame.K_SPACE] and circle_x < RECTANGLE_POS_X[3] + RECTANGLE_WIDTH:
                level = "Level 4"
                rectangle_player.x = RECTANGLE_PLAYER_X_4
                rectangle_player.y = RECTANGLE_PLAYER_Y_4
                RECTANGLE_PLAYER_WIDTH = 40
                RECTANGLE_PLAYER_HEIGHT = 40
                PLAYER_COLOR = WHITE

    if level == "Level 1":
        if rectangle_player.colliderect(RED_GREEN[0]):
            RED_GREEN_COLOR[0] = GREEN
            KOD.append(1)
        if rectangle_player.colliderect(RED_GREEN[1]):
            RED_GREEN_COLOR[1] = GREEN
            KOD.append(2)
        if rectangle_player.colliderect(RED_GREEN[2]):
            RED_GREEN_COLOR[2] = GREEN
            KOD.append(3)
        if rectangle_player.colliderect(RED_GREEN[3]):
            RED_GREEN_COLOR[3] = GREEN
            KOD.append(4)
        if rectangle_player.colliderect(RED_GREEN[4]):
            RED_GREEN_COLOR[4] = GREEN
            KOD.append(5)

        for trail_x in trail:
            if rectangle_player.colliderect(trail_x):
                WIN.fill(BLACK)
                rectangle_player.x = RECTANGLE_PLAYER_X_1
                rectangle_player.y = RECTANGLE_PLAYER_Y_1
                trail = []
                KOD = []
                for i in range(len(RED_GREEN)):
                    RED_GREEN_COLOR[i] = RED
                break

        if 1 in KOD and 2 in KOD and 3 in KOD and 4 in KOD and 5 in KOD:
            KOD = []
            trail = []
            rectangle_player.x, rectangle_player.y = RECTANGLE_PLAYER_X_1, RECTANGLE_PLAYER_Y_1
            for i in range(len(RED_GREEN)):
                RED_GREEN_COLOR[i] = RED
            level = "Huvudmeny"
            circle_x, circle_y = START_POS_X_HUVUDMENY, START_POS_Y_HUVUDMENY

        for wall in WALLS1:
            if rectangle_player.colliderect(wall):
                if abs(wall.top - rectangle_player.bottom) < COLLISION_TOLERANCE:
                    rectangle_player.y -= RECTANGLE_SPEED
                    pygame.draw.rect(WIN, RED, (rectangle_player.x-RECTANGLE_SPEED, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))
                if abs(wall.bottom - rectangle_player.top) < COLLISION_TOLERANCE:
                    rectangle_player.y += RECTANGLE_SPEED
                    pygame.draw.rect(WIN, RED, (rectangle_player.x, rectangle_player.y-RECTANGLE_SPEED, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))
                if abs(wall.left - rectangle_player.right) < COLLISION_TOLERANCE:
                    rectangle_player.x -= RECTANGLE_SPEED
                    pygame.draw.rect(WIN, RED, (rectangle_player.x+RECTANGLE_PLAYER_WIDTH, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))
                    pygame.draw.rect(WIN, RED, (rectangle_player.x, rectangle_player.y+RECTANGLE_PLAYER_HEIGHT, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))
                if abs(wall.right - rectangle_player.left) < COLLISION_TOLERANCE:
                    rectangle_player.x += RECTANGLE_SPEED
                    pygame.draw.rect(WIN, RED, (rectangle_player.x, rectangle_player.y+RECTANGLE_PLAYER_HEIGHT, RECTANGLE_PLAYER_WIDTH, RECTANGLE_SPEED))
                    pygame.draw.rect(WIN, RED, (rectangle_player.x-RECTANGLE_SPEED, rectangle_player.y, RECTANGLE_SPEED, RECTANGLE_PLAYER_HEIGHT))


    elif level == "Level 2":
        for wall in WALLS2:
            if rectangle_player.colliderect(wall):
                if abs(wall.top - rectangle_player.bottom) < COLLISION_TOLERANCE:
                    rectangle_player.y -= RECTANGLE_SPEED
                if abs(wall.bottom - rectangle_player.top) < COLLISION_TOLERANCE:
                    rectangle_player.y += RECTANGLE_SPEED
                if abs(wall.left - rectangle_player.right) < COLLISION_TOLERANCE:
                    rectangle_player.x -= RECTANGLE_SPEED
                if abs(wall.right - rectangle_player.left) < COLLISION_TOLERANCE:
                    rectangle_player.x += RECTANGLE_SPEED

        if rectangle_player.colliderect(box):
            if abs(box.top - rectangle_player.bottom) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH > 20:
                box.y += RECTANGLE_SPEED
            if abs(box.bottom - rectangle_player.top) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH > 20:
                box.y -= RECTANGLE_SPEED
            if abs(box.right - rectangle_player.left) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH > 20:
                box.x -= RECTANGLE_SPEED
            if abs(box.left - rectangle_player.right) < COLLISION_TOLERANCE:
                rectangle_player.x -= RECTANGLE_SPEED
            if abs(box.top - rectangle_player.bottom) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH < 40:
                rectangle_player.y -= RECTANGLE_SPEED
            if abs(box.bottom - rectangle_player.top) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH < 40:
                rectangle_player.y += RECTANGLE_SPEED
            if abs(box.right - rectangle_player.left) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH < 40:
                rectangle_player.x += RECTANGLE_SPEED


        if box.colliderect(box_stop_1):
            box.y += RECTANGLE_SPEED
            rectangle_player.y += RECTANGLE_SPEED

        if box.colliderect(box_stop_2):
            box.y -= RECTANGLE_SPEED
            rectangle_player.y -= RECTANGLE_SPEED

        if rectangle_player.colliderect(goal):
            level = "Huvudmeny"
            circle_x, circle_y = START_POS_X_HUVUDMENY, START_POS_Y_HUVUDMENY

        if rectangle_player.colliderect(grow_button):
            RECTANGLE_PLAYER_WIDTH = 40
            RECTANGLE_PLAYER_HEIGHT = 40
            rectangle_player = pygame.Rect(rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH,RECTANGLE_PLAYER_HEIGHT)
        elif rectangle_player.colliderect(shrink_button):
            RECTANGLE_PLAYER_WIDTH = 20
            RECTANGLE_PLAYER_HEIGHT = 20
            rectangle_player = pygame.Rect(rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH,RECTANGLE_PLAYER_HEIGHT)


    elif level == "Level 3":
        for wall in WALLS3:
            if rectangle_player.colliderect(wall):
                if abs(wall.top - rectangle_player.bottom) < COLLISION_TOLERANCE:
                    rectangle_player.y -= RECTANGLE_SPEED
                if abs(wall.bottom - rectangle_player.top) < COLLISION_TOLERANCE:
                    rectangle_player.y += RECTANGLE_SPEED
                if abs(wall.left - rectangle_player.right) < COLLISION_TOLERANCE:
                    rectangle_player.x -= RECTANGLE_SPEED
                if abs(wall.right - rectangle_player.left) < COLLISION_TOLERANCE:
                    rectangle_player.x += RECTANGLE_SPEED


        if rectangle_player.colliderect(box_3):
            if abs(box_3.top - rectangle_player.bottom) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH > 20:
                box_3.y += RECTANGLE_SPEED
            if abs(box_3.bottom - rectangle_player.top) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH > 20:
                box_3.y -= RECTANGLE_SPEED
                timer_start = pygame.time.get_ticks()
            if abs(box_3.left - rectangle_player.right) < COLLISION_TOLERANCE:
                rectangle_player.x -= RECTANGLE_SPEED
            if abs(box_3.right - rectangle_player.left) < COLLISION_TOLERANCE:
                rectangle_player.x += RECTANGLE_SPEED
            if abs(box_3.top - rectangle_player.bottom) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH < 40:
                rectangle_player.y -= RECTANGLE_SPEED
            if abs(box_3.bottom - rectangle_player.top) < COLLISION_TOLERANCE and RECTANGLE_PLAYER_WIDTH < 40:
                rectangle_player.y += RECTANGLE_SPEED

        if box_3.y == 0:
            rectangle_player.y += RECTANGLE_SPEED
            box_3.y += RECTANGLE_SPEED

        if rectangle_player.colliderect(goal_3):
            level = "Huvudmeny"
            circle_x, circle_y = START_POS_X_HUVUDMENY, START_POS_Y_HUVUDMENY

        timer_start = timer(current_time, timer_start)

        if rectangle_player.colliderect(grow_button_3):
            RECTANGLE_PLAYER_WIDTH = 40
            RECTANGLE_PLAYER_HEIGHT = 40
            rectangle_player = pygame.Rect(rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT)
        elif rectangle_player.colliderect(shrink_button_3):
            RECTANGLE_PLAYER_WIDTH = 20
            RECTANGLE_PLAYER_HEIGHT = 20
            rectangle_player = pygame.Rect(rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT)

    elif level == "Level 4":

        for wall in WALLS4:
            if rectangle_player.colliderect(wall):
                wall_collision_4(wall, rectangle_player)

        for wall in BLUE_WALLS:
            if rectangle_player.colliderect(wall) and PLAYER_COLOR != BLUE:
                wall_collision_4(wall, rectangle_player)

        for wall in YELLOW_WALLS:
            if rectangle_player.colliderect(wall) and PLAYER_COLOR != YELLOW:
                wall_collision_4(wall, rectangle_player)

        if rectangle_player.colliderect(RED_CHANGE) and PLAYER_COLOR != DARK_GREEN and PLAYER_COLOR != YELLOW:
            PLAYER_COLOR = RED
        elif rectangle_player.colliderect(RED_CHANGE):
            PLAYER_COLOR = YELLOW

        if rectangle_player.colliderect(ORANGE_CHANGE):
            PLAYER_COLOR = ORANGE

        if rectangle_player.colliderect(PURPLE_CHANGE):
            PLAYER_COLOR = PURPLE

        if rectangle_player.colliderect(BROWN_CHANGE):
            PLAYER_COLOR = BROWN

        if rectangle_player.colliderect(TURQUOISE_CHANGE):
            PLAYER_COLOR = TURQUOISE

        if rectangle_player.colliderect(PINK_CHANGE):
            PLAYER_COLOR = PINK

        if rectangle_player.colliderect(BEIGE_CHANGE):
            PLAYER_COLOR = BEIGE

        if rectangle_player.colliderect(BLUE_CHANGE):
            PLAYER_COLOR = BLUE

        if rectangle_player.colliderect(DARK_GREEN_CHANGE) and PLAYER_COLOR != RED and PLAYER_COLOR != YELLOW:
            PLAYER_COLOR = DARK_GREEN
        elif rectangle_player.colliderect(DARK_GREEN_CHANGE):
            PLAYER_COLOR = YELLOW

        if rectangle_player.colliderect(goal_4):
            level = "Huvudmeny"
            circle_x, circle_y = START_POS_X_HUVUDMENY, START_POS_Y_HUVUDMENY

    return level, trail, KOD, circle_x, circle_y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, rectangle_player, timer_start, PLAYER_COLOR


def main(RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, timer_start, PLAYER_COLOR):
    clock = pygame.time.Clock()
    level = "Huvudmeny"
    trail = [pygame.Rect(0, 0, 0, 0)]
    KOD = []

    circle_x, circle_y = START_POS_X_HUVUDMENY, START_POS_Y_HUVUDMENY
    rectangle_player = pygame.Rect(RECTANGLE_PLAYER_X_1, RECTANGLE_PLAYER_Y_1, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT)

    run = True
    while run:
        rectangle_player = pygame.Rect(rectangle_player.x, rectangle_player.y, RECTANGLE_PLAYER_WIDTH ,RECTANGLE_PLAYER_HEIGHT)
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_TAB]:
            level = "Huvudmeny"
            rectangle_player.x = RECTANGLE_PLAYER_X_1
            rectangle_player.y = RECTANGLE_PLAYER_Y_1
        if keys_pressed[pygame.K_BACKSPACE]:
            run = False

        window(level, circle_x, circle_y, rectangle_player, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, PLAYER_COLOR)
        circle_x, circle_y, rectangle_player, trail = movement(keys_pressed, circle_x, circle_y, level, rectangle_player, trail, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT)
        level, trail, KOD, circle_x, circle_y, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, rectangle_player, timer_start, PLAYER_COLOR = collision(circle_x, circle_y, keys_pressed, level, rectangle_player, RED_GREEN_COLOR, trail, KOD, box, RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, current_time, timer_start, PLAYER_COLOR)


main(RECTANGLE_PLAYER_WIDTH, RECTANGLE_PLAYER_HEIGHT, timer_start, PLAYER_COLOR)