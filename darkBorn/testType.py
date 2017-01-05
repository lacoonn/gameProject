import pygame

a = 1.5 # 가속도
# v = 이전속도 + at (t는 프레임으로 대체)
WIDTH = 800
HEIGHT = 500
GROUND = HEIGHT - 100


class character:
    image = None

    def __init__(self, x_pos, y_pos, x_v, y_v):
        self.x_pos = x_pos # 위치
        self.y_pos = y_pos
        self.x_v = x_v # 속도
        self.y_v = y_v


def drawObject(object, x, y): # 객체를 인자로 받아서 화면에 출력
    global gamepad
    gamepad.blit(object, (x, y))


def updateObject(object): # 객체의 속도와 위치를 업데이트
    object.y_v = object.y_v - a;
    object.x_pos = object.x_pos + object.x_v
    if object.y_pos - object.y_v > GROUND: # 다음에 이동할 위치가 땅보다 아래면 땅으로 이동
        object.y_pos = GROUND
        object.y_v = 0
    else:
        object.y_pos = object.y_pos - object.y_v


def runGame(): # 게임에서 작동하는 부분. 무한반복문
    global gamepad, clock
    global player

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN: # 키입력을 받으면 거기에 해당하는 결과를 냄
                if event.key == pygame.K_RIGHT:
                    player.x_v = 7
                if event.key == pygame.K_LEFT:
                    player.x_v = -7
                if event.key == pygame.K_UP:
                    if player.y_pos == GROUND: # 땅 위에 있을때만 점프 가능
                        player.y_v = 25
            if event.type == pygame.KEYUP: # 해당 방향으로 이동하고 있을 때만 키를 땠을때 속도를 0으로 변환
                if event.key == pygame.K_RIGHT:
                    if player.x_v > 0:
                        player.x_v = 0
                elif event.key == pygame.K_LEFT:
                    if player.y_v < 0:
                        player.x_v = 0

        gamepad.fill((255, 255, 255))

        # 상태 업데이트하는 부분
        updateObject(player)

        # 그림 그리는 부분
        drawObject(player.image, player.x_pos, player.y_pos)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()







def initGame(): # 게임 초기화하는 함수
    global gamepad, clock
    global player
    player = character(100, 0, 0, 0)

    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))
    player.image = pygame.image.load('player.png')

    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()