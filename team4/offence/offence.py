HEIGHT = 600
WIDTH = 900

from offence_strategy import OffenceStrategy
import random

number_0f_aliens = random.randint(1, 10)
offence_image = 'rock1'

aliens = []
offences = []

for i in range(number_0f_aliens):
    alien = Actor(offence_image)
    offence = OffenceStrategy(actor=alien, width=WIDTH, height=HEIGHT)
    aliens.append(alien)
    offences.append(offence)

def draw():
    screen.fill((0, 128, 0))
    for alien in aliens:
        alien.draw()

def update():
    for offence in offences:
        offence.next_location()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()

def set_alien_normal():
    alien.image = 'alien'