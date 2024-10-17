import pygame
import pymunk
import pymunk.pygame_util
import random

# Initialize Pygame and Pymunk
pygame.init()
space = pymunk.Space()
space.gravity = (0, 0)

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Musical Marbles")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MARBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 128, 128)]

# Create walls
walls = [
    pymunk.Segment(space.static_body, (50, 50), (750, 50), 5),
    pymunk.Segment(space.static_body, (750, 50), (750, 550), 5),
    pymunk.Segment(space.static_body, (750, 550), (50, 550), 5),
    pymunk.Segment(space.static_body, (50, 550), (50, 50), 5)
]
for wall in walls:
    wall.elasticity = 0.9
    wall.friction = 0.5
space.add(*walls)

# Create marbles
marbles = []
for i in range(7):
    mass = 1
    radius = 20
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    body.position = x, y
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9
    shape.friction = 0.5
    shape.color = MARBLE_COLORS[i]
    space.add(body, shape)
    marbles.append(shape)

# Set up sounds
pygame.mixer.init()
sounds = {}
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for i, note in enumerate(notes):
    sounds[f'marble_{i}'] = pygame.mixer.Sound(f'{note}.wav')
for i in range(4):
    sounds[f'wall_{i}'] = pygame.mixer.Sound(f'{notes[i]}_wall.wav')

def play_collision_sound(arbiter, space, data):
    for shape in arbiter.shapes:
        if shape in marbles:
            marble_index = marbles.index(shape)
            if arbiter.shapes[0] in walls or arbiter.shapes[1] in walls:
                wall_index = walls.index(arbiter.shapes[0] if arbiter.shapes[0] in walls else arbiter.shapes[1])
                sounds[f'wall_{wall_index}'].play()
            else:
                other_marble = arbiter.shapes[0] if shape != arbiter.shapes[0] else arbiter.shapes[1]
                other_marble_index = marbles.index(other_marble)
                sound_index = (marble_index + other_marble_index) % 7
                sounds[f'marble_{sound_index}'].play()
    return True

# Add collision handler
handler = space.add_collision_handler(0, 0)
handler.begin = play_collision_sound

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle arrow key presses to tilt the box
    keys = pygame.key.get_pressed()
    tilt_force = 500
    if keys[pygame.K_LEFT]:
        space.gravity = (-tilt_force, space.gravity.y)
    elif keys[pygame.K_RIGHT]:
        space.gravity = (tilt_force, space.gravity.y)
    else:
        space.gravity = (0, space.gravity.y)

    if keys[pygame.K_UP]:
        space.gravity = (space.gravity.x, -tilt_force)
    elif keys[pygame.K_DOWN]:
        space.gravity = (space.gravity.x, tilt_force)
    else:
        space.gravity = (space.gravity.x, 0)

    # Update physics
    space.step(1/60.0)

    # Draw everything
    screen.fill(WHITE)
    for wall in walls:
        pygame.draw.line(screen, BLACK, wall.a, wall.b, 5)
    for marble in marbles:
        pygame.draw.circle(screen, marble.color, marble.body.position, 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
