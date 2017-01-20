import pygame
import swordsman as swm

WIDTH = 1280
HEIGHT = 720
pygame.font.init()
LARGEFONT = pygame.font.Font('D2Coding.ttc', 100)
FONT = pygame.font.Font('D2Coding.ttc', 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)



def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    runGame()


def runGame():
    global gamepad, clock
    stage = 0

    #메뉴 목록
    menuList = ['게임시작', '게임종료']

    while True:
        isMenu = True
        menuPoint = 0
        while isMenu is True: # 메뉴화면일 경우
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if menuPoint > 0:
                            menuPoint -= 1
                    if event.key == pygame.K_DOWN:
                        if menuPoint < len(menuList):
                            menuPoint += 1
                    if event.key == pygame.K_RETURN:
                        if menuPoint == 0:
                            isMenu = False
                        if menuPoint == len(menuList)-1:
                            pygame.quit()
            # 화면 업데이트 및 출력
            gamepad.fill(BLACK)
            text = LARGEFONT.render('War Simulator', True, WHITE)
            gamepad.blit(text, (300, 200))
            for i in range(len(menuList)):
                if i == menuPoint:
                    text = FONT.render(menuList[i], True, RED)
                else:
                    text = FONT.render(menuList[i], True, WHITE)
                gamepad.blit(text, (300, 400 + i * 100))

            pygame.display.update()
            clock.tick(60)

        while isMenu is False: # 메뉴화면이 아닐 경우(시뮬실행중)
            ch1 = swm.swordsman('img_src/swordsman.png', (30, 30))
            ch1.update()
            print(ch1.rect)
            pygame.quit()
            # 화면 업데이트 및 출력
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
    initGame()
