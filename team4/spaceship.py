from math import sin, cos, radians

HEIGHT = 600
WIDTH = 900

alien = Actor('player')

alien.pos = (500,500)

state = {
    "direction" : 0,
    "moving" : 0
}
    
def draw():
    screen.fill((0, 0, 0))
    alien.draw()

def on_key_down(key):
    print(key)
    if key == keys.UP:
        state["moving"] = not state["moving"]
    elif key == keys.DOWN:
        state["moving"] = not state["moving"]
    
    print(alien.angle)

def update():
    if keyboard.RIGHT :
        alien.angle += 2
        state["direction"] = (state["direction"] - radians(alien.angle))
    elif keyboard.LEFT:
        alien.angle -= 2
        state["direction"] = (state["direction"] + radians(alien.angle))

    if state["moving"]:
        newX = sin(state["direction"])
        newY = cos(state["direction"])
        alien.x -= newX * 10
        alien.y -= newY * 10
