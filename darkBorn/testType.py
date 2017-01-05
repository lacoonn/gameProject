import pygame

a = 2 # 가속도
# v = 이전속도 + at (t는 프레임으로 대체)
WIDTH = 1600
HEIGHT = 900


class character:
    def __init__(self, x_pos, y_pos, x_v, y_v):
        self.x_pos = x_pos # 위치
        self.y_pos = y_pos
        self.x_v = x_v # 속도
        self.y_v = y_v

def runGame():



def initGame():
    global gamepad
    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))
    runGame()


ch = character(1, 1, 1, 1)
print(ch.x_pos)

if __name__ == '__main__':
    initGame()