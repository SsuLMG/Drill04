from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('rockman.png')

left_right = None
def handle_events():
    global running, dir, wid, left_right

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                left_right = True
                dir += 1
            elif event.key == SDLK_LEFT:
                left_right = False
                dir -= 1
            elif event.key == SDLK_UP:
                left_right = True
                wid += 1
            elif event.key == SDLK_DOWN:
                left_right = True
                wid -= 1

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                wid -= 1
            elif event.key == SDLK_DOWN:
                wid += 1

running = True
frame = 0
dir = 0
wid = 0

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    clear_canvas()
    tuk_ground.draw(640,512)

    if left_right is True:
        character.clip_draw(frame * 172, 0, 172, 183, x, y, 100, 100)
    elif left_right is False:
        character.clip_composite_draw(frame * 172, 0, 172, 183, 0, 'h', x, y, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    x += dir * 5
    y += wid * 5
    if x >= TUK_WIDTH:
        x = TUK_WIDTH
    if y >= TUK_HEIGHT-183//2:
        y = TUK_HEIGHT-183//2
    if x < 0:
        x = 0
    if y < 0+183//2:
        y = 0+183//2
    delay(0.01)

close_canvas()