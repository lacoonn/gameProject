import pygame
import math, sys

class swordsman(pygame.sprite.Sprite):
    hp = 300
    invin = False
    atk = 30
    reach = 10
    xSpeed = 3
    ySpeed = 1
    # 이동을 판단하는 AI에 집어넣을 예정
    goRight = 1
    goDown = 1

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_normal = pygame.image.load(image)
        self.position = position

        self.image = self.image_normal # 다른 이미지 사용해야할지도 몰라서 이렇게 해놓음
        self.rect = self.image.get_rect()
        self.rect.center = self.position # rect는 position을 중심으로 하는 사각형

    def update(self, enemy_group):
        # enemy_group는 sprite의 group 형식으로 줘야함
        xPos = self.position[0]
        yPos = self.position[1]
        # 목표 판단
        enemy = self.judgement(enemy_group)
        # 방향 설정
        ex, ey = enemy.position
        if ex > xPos:
            self.goRight = 1
        elif ex == xPos:
            self.goRight = 0
        else:
            self.goRight = -1
        if ey > yPos:
            self.goDown = 1
        elif ey == yPos:
            self.goDown = 0
        else:
            self.goDown = -1
        # 사거리 판단 및 공격
        atk_rect = self.rect.move(self.goRight*self.reach, 0) # 공격 범위
        if atk_rect.colliderect(enemy.rect):
            self.attack()
        # 보는 방향에 따라 위치를 업데이트
        xPos += self.xSpeed * self.goRight
        yPos += self.ySpeed * self.goDown
        self.position = (xPos, yPos)

        if self.goRight == 1:
            self.image = self.image_normal # 다른 이미지 사용해야할지도 몰라서 이렇게 해놓음
        elif self.goRight == -1:
            self.image = pygame.transform.flip(self.image_normal, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = self.position # rect는 position을 중심으로 하는 사각형

    def attack(self):
        print('ATTACK!!!')
        self.goDown = 0
        self.goRight = 0
        # collisions = pygame.sprite.spritecollide(self, enemy_group, False)

    def judgement(self, enemy_group):
        # 가장 가까운 적 판단
        enemy_list = enemy_group.sprites()
        mindis_enemy = None
        for enemy in enemy_list:
            if mindis_enemy == None:
                mindis_enemy = enemy
            else:
                prev_dis = self.get_distance(self.position, mindis_enemy.position)
                now_dis = self.get_distance(self.position, enemy.position)
                if prev_dis > now_dis:
                    mindis_enemy = enemy
        return mindis_enemy

    def get_distance(self, origin, destination):
        ox, oy = origin
        dx, dy = destination
        return (ox-dx)*(ox-dx) + (oy-dy)*(oy-dy)
