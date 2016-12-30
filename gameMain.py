import pygame as pg
import random
from time import sleep


WHITE = (255, 255, 255)
WIDTH = 1024
HEIGHT = 512
background_width = 1024
aircraft_width = 90
aircraft_height = 55

bat_width = 110
bat_height = 67

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))


def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))


def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet, boom

    isShotBat = False
    boom_count = 0

    bullet_xy = []

    x = WIDTH * 0.05
    y = HEIGHT * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    bat_x = WIDTH
    bat_y = random.randrange(0, HEIGHT)

    fire_x = WIDTH
    fire_y = random.randrange(0, HEIGHT)
    random.shuffle(fires)
    fire = fires[0]



    crashed = False
    while not crashed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    y_change = -5
                elif event.key == pg.K_DOWN:
                    y_change = +5
                elif event.key == pg.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height/2
                    bullet_xy.append([bullet_x, bullet_y])

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_change = 0

        gamepad.fill(WHITE)
        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x = background_width
        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

        # Aircraft Position
        y += y_change
        if y < 0:
            y = 0
        elif y > HEIGHT - aircraft_height:
            y = HEIGHT - aircraft_height

        # Bat Position
        bat_x -= 7
        if bat_x <= 0:
            bat_x = WIDTH
            bat_y = random.randrange(0, HEIGHT)

        # Firebll Position
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = WIDTH
            fire_y = random.randrange(0, HEIGHT)
            random.shuffle(fires)
            fire = fires[0]

        # Bullets Position



        airplane(x, y)
        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()


def initGame():
    global gamepad, clock, aircraft

    pg.init()
    gamepad = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('gameProject')
    aircraft = pg.image.load('airplane.jpg')

    clock = pg.time.Clock()
    runGame()

# I edittedd!!!!!!!!!
# I'm Mr.Jo

if __name__ == '__main__':
    initGame()
