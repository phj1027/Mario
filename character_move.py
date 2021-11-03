from pico2d import *

open_canvas(800, 450)

background = load_image('background.png')
character_wr = load_image('walk_animation_mario.png')
character_wl = load_image('walk_animation_mario_left.png')

def handle_events():
    global running
    global dir
    global state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN: #and event.key == SDLK_ESCAPE:
           if event.key == SDLK_RIGHT:
               dir += 1
           elif event.key == SDLK_LEFT:
               dir -= 1
           elif event.key == SDLK_ESCAPE:
               running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
    pass

running = True
x = 800 // 2 #캐릭터 가운데위치
frame = 0 #3개
dir = 0 #방향변수 -1left +1right
state = 0 #키를 뗐을때 방향상태 2right 3left

while running:
    clear_canvas()
    background.draw(400, 225)
    character_wr.clip_draw(frame * 55, 0, 55, 30, x, 75)

    if dir == 1:
        character_wr.clip_draw(frame * 55, 0, 55, 30, x, 75)
        frame = (frame + 1) % 3
        x += dir * 8

    elif dir == -1:
        character_wl.clip_draw(frame * 55, 0, 55, 30, x, 75)
        frame = (frame + 1) % 3
        x += dir * 8

    update_canvas()
    handle_events()
    delay(0.1)
    #get_events()

close_canvas()
