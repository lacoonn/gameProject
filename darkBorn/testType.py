import pygame

a = 1.5 # 가속도
# v = 이전속도 + at (t는 프레임으로 대체)
WIDTH = 800
HEIGHT = 500
GROUND = HEIGHT - 140


class character:
    image = None
    width = 0
    height = 0
    view_dir = True # 보는 방향, True는 오른쪽
    weapon = None
    weapon_temp = None
    weapon_x = None
    weapon_y = None
    isAttack = False
    rotateTime = 0
    isGround = True

    def __init__(self, x_pos1, y_pos1, x_v1, y_v1):
        self.x_pos = x_pos1 # 위치
        self.y_pos = y_pos1
        self.x_v = x_v1 # 속도
        self.y_v = y_v1

    def setImage(self, filename):
        self.image = pygame.image.load(filename)
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]

    def setWeapon(self, filename):
        self.weapon = pygame.image.load(filename)
        if self.view_dir is True:
            self.weapon_x = self.x_pos + self.width*2/3
        elif self.view_dir is False:
            self.weapon_x = self.x_pos - 40
        self.weapon_y = self.y_pos

    def updateWeapon(self):
        if self.view_dir is True:
            self.weapon_x = self.x_pos + self.width*2/3
        elif self.view_dir is False:
            self.weapon_x = self.x_pos - 40
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

class ground:
    image = None
    width = 0
    height = 0
    x_v = 0
    y_v = 0

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def setImage(self, filename):
        self.image = pygame.image.load(filename)
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]


def collison(object1, object2):
    if object1.x_pos < object2.x_pos + object2.width and\
    object1.x_pos + object1.width > object2.x_pos + object2.x_v and\
    object1.y_pos < object2.y_pos + object2.height and\
    object1.y_pos + object1.height > object2.y_pos + object2.y_v:
        return True
    else:
        return False


def drawObject(object): # 객체를 인자로 받아서 화면에 출력
    global gamepad

    if object.view_dir is True: # 플레이어가 보는 방향이 오른쪽이면
        gamepad.blit(object.image, (object.x_pos, object.y_pos))
        if object.isAttack is True:
            object.attack()
        gamepad.blit(object.weapon, (object.weapon_x, object.weapon_y))

    if object.view_dir is False: # 플레이어가 보는 방향이 왼쪽이면
        gamepad.blit(pygame.transform.flip(object.image, True, False), (object.x_pos, object.y_pos))
        if object.isAttack is True:
            object.attack()
        gamepad.blit(pygame.transform.flip(object.weapon, True, False), (object.weapon_x, object.weapon_y))


def updateCharacter(object): # 객체의 속도와 위치를 업데이트
    global groundGroup # 임시로

    # 오브젝트의 y 속력
    object.y_v = object.y_v - a
    # 오브젝트의 x 위치
    object.x_pos = object.x_pos + object.x_v

    # 플레이어가 벽 밖으로 나가는 것을 막는다
    if object.x_pos < 0:
        object.x_pos = 0
    if object.x_pos + object.width > WIDTH:
        object.x_pos = WIDTH - object.width

    # 다음에 이동할 위치가 땅보다 아래면 땅으로 이동
    if object.y_pos - object.y_v > GROUND:
        object.y_pos = GROUND
        object.y_v = 0
    else:
        # 아니면 속도만큼 y 위치를 옮긴다
        object.y_pos = object.y_pos - object.y_v

    for temp1 in groundGroup:
        if collison(object, temp1) is True:
            # 이전의 위치를 갖는 변수(충돌 방향 판단을 위해)
            prev_x = object.x_pos - object.x_v
            prev_y = object.y_pos + object.y_v
            # 오브젝트가 위에서 그라운드에 충돌하면 서있는다
            if prev_y + object.height <= temp1.y_pos:
                object.y_pos = temp1.y_pos - object.height
                object.y_v = 0
            # 오브젝트가 아래에서 충돌하면 부딪힌다
            if prev_y >= temp1.y_pos + temp1.height:
                object.y_pos = temp1.y_pos + temp1.height
                object.y_v = 0
            # 오브젝트가 우측으로 충돌하면 부딪힌다
            if prev_x + object.width <= temp1.x_pos:
                object.x_pos = temp1.x_pos - object.width
                object.x_v = 0
                # object.y_v = 0
            # 오브젝트가 좌측으로 충돌하면 부딪힌다
            if prev_x >= temp1.x_pos + temp1.width:
                object.x_pos = temp1.x_pos + temp1.width
                object.x_v = 0
                # object.y_v = 0

    # 플레이어가 점프할 수 있는지(땅에 있는지) 판단한다
    object.isGround = False
    for temp2 in groundGroup:
        if object.y_pos + object.height == temp2.y_pos:
            object.isGround = True
    if object.y_pos == GROUND:
        object.isGround = True


    player.updateWeapon()


def runGame(): # 게임에서 작동하는 부분. 무한반복문
    global gamepad, clock
    global player, background, groundGroup

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
                    if player.isGround == True: # 땅 위에 있을때만 점프 가능
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

        # 배경을 그리는 부분
        gamepad.fill((255, 255, 255))
        gamepad.blit(background, (0, 0))


        # 상태 업데이트하는 부분
        updateCharacter(player)

        # 그림 그리는 부분
        for temp1 in groundGroup:
            gamepad.blit(temp1.image, (temp1.x_pos, temp1.y_pos))
        drawObject(player)


        # 설정
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def initGame(): # 게임 초기화하는 함수
    global gamepad, clock
    global player, background, groundGroup

    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.image.load('background.png')

    groundGroup = []

    ground1 = ground(300, HEIGHT - 250)
    ground1.setImage('ground.png')
    groundGroup.append(ground1)

    ground2 = ground(500, HEIGHT - 400)
    ground2.setImage('ground.png')
    groundGroup.append(ground2)

    player = character(100, 0, 0, 0)
    player.setImage('player.png')
    player.setWeapon('sword.png')
    player.updateWeapon()

    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__':
    initGame()
