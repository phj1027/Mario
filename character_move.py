from pico2d import *

open_canvas(800, 450)

background = load_image('background.png')
character = load_image('walk_animation_mario.png')

running = True
x = 0
frame = 0 #3개

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass

while x < 800 and running:
    clear_canvas()
    background.draw(400, 225)
    character.clip_draw(frame * 55, 0, 55, 30, x, 75)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 3
    x += 5
    delay(0.1)

    #get_events()

close_canvas()
