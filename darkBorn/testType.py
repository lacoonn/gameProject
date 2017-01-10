import pygame

a = 1.5 # 가속도
# v = 이전속도 + at (t는 프레임으로 대체)
WIDTH = 800
HEIGHT = 500
GROUND = HEIGHT - 100


class character:
    image = None
    view_dir = True # 보는 방향, True는 오른쪽
    weapon = None
    weapon_temp = None
    weapon_x = None
    weapon_y = None
    isAttack = False
    rotateTime = 0

    def __init__(self, x_pos1, y_pos1, x_v1, y_v1):
        self.x_pos = x_pos1 # 위치
        self.y_pos = y_pos1
        self.x_v = x_v1 # 속도
        self.y_v = y_v1

    def updateWeapon(self):
        if self.view_dir is True:
            self.weapon_x = self.x_pos + self.image.get_size()[0]*2/3
        elif self.view_dir is False:
            self.weapon_x = self.x_pos
        self.weapon_y = self.y_pos

    def attack(self):
        if self.isAttack is True:
            self.rotateTime += 1
            if self.rotateTime is 2:
                self.weapon = pygame.image.load('sword0.png')
            if self.rotateTime is 4:
                self.weapon = pygame.image.load('sword1.png')
            if self.rotateTime is 6:
                self.weapon = pygame.image.load('sword2.png')
            if self.rotateTime is 8:
                self.weapon = pygame.image.load('sword3.png')
            if self.rotateTime is 10:
                self.weapon = pygame.image.load('sword4.png')
            if self.rotateTime is 12:
                self.isAttack = False
                self.weapon = self.weapon_temp
                self.rotateTime = 0
                return
        else:
            self.isAttack = True
            self.weapon_temp = self.weapon.copy()




def drawObject(object): # 객체를 인자로 받아서 화면에 출력
    global gamepad

    if object.view_dir is True:
        gamepad.blit(object.image, (object.x_pos, object.y_pos))
        if object.isAttack is True:
            object.attack()
        gamepad.blit(object.weapon, (object.weapon_x, object.weapon_y))

    if object.view_dir is False:
        gamepad.blit(pygame.transform.flip(object.image, True, False), (object.x_pos, object.y_pos))
        if object.isAttack is True:
            object.attack()
        gamepad.blit(pygame.transform.flip(object.weapon, True, False), (object.weapon_x, object.weapon_y))


def updateObject(object): # 객체의 속도와 위치를 업데이트
    object.y_v = object.y_v - a;
    object.x_pos = object.x_pos + object.x_v
    if object.y_pos - object.y_v > GROUND: # 다음에 이동할 위치가 땅보다 아래면 땅으로 이동
        object.y_pos = GROUND
        object.y_v = 0
    else:
        object.y_pos = object.y_pos - object.y_v
    player.updateWeapon()


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
                    player.view_dir = True
                if event.key == pygame.K_LEFT:
                    player.x_v = -7
                    player.view_dir = False
                if event.key == pygame.K_UP:
                    if player.y_pos == GROUND: # 땅 위에 있을때만 점프 가능
                        player.y_v = 25
                if event.key is pygame.K_z:
                    player.attack()
            if event.type == pygame.KEYUP: # 해당 방향으로 이동하고 있을 때만 키를 땠을때 속도를 0으로 변환
                if event.key == pygame.K_RIGHT:
                    if player.x_v > 0:
                        player.x_v = 0
                elif event.key == pygame.K_LEFT:
                    if player.x_v < 0:
                        player.x_v = 0

        gamepad.fill((255, 255, 255))

        # 상태 업데이트하는 부분
        updateObject(player)

        # 그림 그리는 부분
        drawObject(player)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()







def initGame(): # 게임 초기화하는 함수
    global gamepad, clock
    global player

    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))

    player = character(100, 0, 0, 0)
    player.image = pygame.image.load('player.png')
    player.weapon = pygame.image.load('sword.png')
    player.updateWeapon()

    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()