# Musical Marbles

## Installation

0. Ensure you have Python 3.x installed on your system.
1. Clone this repo, or just download the .tgz file, a gzipped tarball.
2. Install the required dependencies:
   ```
   pip install pygame pymunk
   ```
   Note: On some systems, you may need to use `pip3` instead of `pip`.
3. Download the sound files (C.wav, D.wav, E.wav, F.wav, G.wav, A.wav, B.wav, C_wall.wav, D_wall.wav, E_wall.wav, F_wall.wav) and place them in the same directory as the script.

## How to Play

1. Run the script:
   ```
   python marbles.py
   ```
   Note: On some systems, you may need to use `python3` instead of `python`.
2. Use the arrow keys to tilt the box and move the marbles:
   - Left arrow: Tilt left
   - Right arrow: Tilt right
   - Up arrow: Tilt up
   - Down arrow: Tilt down

3. Watch and listen as the marbles collide with each other and the walls, creating a unique sound experience.

4. To exit the game, close the window or press Ctrl+C in the terminal.

## Features

- 7 colorful marbles, each associated with a musical note
- Physics-based gameplay using Pymunk
- Collision sounds for marble-to-marble and marble-to-wall interactions
- Tiltable play area using arrow keys

Enjoy your musical marble adventure!
