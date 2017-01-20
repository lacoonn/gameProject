# -*- coding: utf-8 -*-

import math, sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)
clock = pygame.time.Clock()

class SimpleSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_src_image = pygame.image.load(image)
        self.user_position = position
        self.user_rotation = 30
        self.user_speed = 0
        self.user_rotation_speed = 0

    def update(self, deltat):
        # 속도, 회전 속도에 따라 위치 정보를 업데이트한다
        self.user_rotation += self.user_rotation_speed
        x, y = self.user_position
        rad = self.user_rotation * math.pi / 180
        x += -self.user_speed * math.sin(rad)
        y += -self.user_speed * math.cos(rad)
        self.user_position = (x, y)

        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

class BlockSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_image_normal = pygame.image.load("sword.png");
        self.user_image_hit = pygame.image.load("sword4.png");
        self.user_position = position;

        self.image = self.user_image_normal
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

    def update(self, hit_list):

        if self in hit_list:
            self.image = self.user_image_hit
        else:
            self.image = self.user_image_normal

        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

rect = screen.get_rect()
simple = SimpleSprite('player.png', rect.center)
simple_group = pygame.sprite.RenderPlain(simple)

blocks = [
    BlockSprite((200, 200)),
    BlockSprite((800, 200)),
    BlockSprite((200, 600)),
    BlockSprite((800, 600))
]
block_group = pygame.sprite.RenderPlain(*blocks)

background = pygame.image.load('background.png')
screen.blit(background, (0,0))

while True:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 키입력에 따라 속도, 회전 속도를 설정
        if hasattr(event, 'key'):
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                simple.user_rotation_speed = down * -5 # 시계 방향이 마이너스인 것에 유의
            elif event.key == K_LEFT:
                simple.user_rotation_speed = down * 5
            elif event.key == K_UP:
                simple.user_speed = down * 10
            elif event.key == K_DOWN:
                simple.user_speed = down * -10

    simple_group.update(deltat)

    collisions = pygame.sprite.spritecollide(simple, block_group, False)
    block_group.update(collisions)

    simple_group.clear(screen, background)
    block_group.clear(screen, background)
    simple_group.draw(screen)
    block_group.draw(screen)
    pygame.display.flip()
