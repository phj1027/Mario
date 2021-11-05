import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

background = None
mario = None
mushroom = None

class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 225)



class Mario:
    def __init__(self):
        self.image = load_image('mario.png')
        self.x, self.y = 0, 81
        self.frame = 0
        self.dir = 1

    def update(self): #소년의 행위 구현 (위치 증가)
        self.frame = (self.frame + 1) % 3
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 50, 50 * 1, 47, 47, self.x, self.y)
        #if dir = -1
            #self 왼쪽달려가는이미지
        #if die = 1
            #self 오른쪾달려가는이미지

class Mushroom:
    def __init__(self):
        self.image = load_image('mushroom.png')
        self.x, self.y = 500, 84
        self.frame = 0
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir
        if self.x >= 600:
            self.dir = -1
        elif self.x <= 400:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)

def enter():
    global mario, background, mushroom
    mario = Mario()
    background = Background()
    mushroom = Mushroom()

def exit():
    global mario, background, mushroom
    del(mario)
    del(background)
    del(mushroom)

def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    mario.update()
    mushroom.update()

def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    mushroom.draw()
    update_canvas()

