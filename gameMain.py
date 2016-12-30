import pygame as pg

WHITE = (255, 255, 255)
WIDTH = 1024
HEIGHT = 512

def runGame():
    global gamepad, clock

    crashed = False
    while not crashed:
        for event in pg.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gamepad.fill(WHITE)
        pg.display.update()
        clock.tick(60)

    pg.quit()
def initGame():
    global gamepad, clock

    pg.init()
    gamepad = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('gameProject')

    clock = pg.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()