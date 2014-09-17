from . import sanneal
from PIL import Image
import math
import random
#import cProfile

IMAGE_WIDTH  = 32
IMAGE_HEIGHT = 32
INITIAL_TEMP = 1.0
TEMP_MOD = 0.00001
TEST_RADIUS = 3

def pixels():
    return [(x, y) for x in range(IMAGE_WIDTH)
                   for y in range(IMAGE_HEIGHT)]


def pixel_neighbors(xy):
    (x, y) = xy
    
    minx = max(0, x-TEST_RADIUS)
    maxx = min(IMAGE_WIDTH-1, x+TEST_RADIUS)
    miny = max(0, y-TEST_RADIUS)
    maxy = min(IMAGE_HEIGHT-1, y+TEST_RADIUS)
    
    return [(i, j) for i in range(minx, maxx+1)
                   for j in range(miny, maxy+1)]


def pair_energy(xy1, value1, xy2, value2):
    if xy1 == xy2 or value1 != value2:
        return 0
    
    (x1, y1) = xy1
    (x2, y2) = xy2
    
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    # Nearby pixels of same color attract each other at short range
    return -math.exp(-dist)


def pixel_energy(xy, state):
    energy = 0
    value = state.getpixel(xy)
    for n in pixel_neighbors(xy):
        energy += pair_energy(xy, value, n, state.getpixel(n))
    return energy
    

# Should only be called once -- calculating energy from scratch is very slow.
def get_energy(state):
    energy = 0
    for p in pixels():
        energy += pixel_energy(p, state)
    return energy


# Returns a 2-tuple: a random neighboring state and its energy.
def get_neighbor(state, energy):
    # Choose two neighboring pixels to swap
    orientation = random.randint(0,1)  # 0: horizontal, 1: vertical
    xy1 = (x1, y1) = (random.randint(0, IMAGE_WIDTH  - 2 + orientation),
                      random.randint(0, IMAGE_HEIGHT - 1 - orientation))
    xy2 = (x1 + 1 - orientation,
           y1 + orientation)

    # Swap the pixels
    nstate = state.copy()
    value1 = nstate.getpixel(xy1)
    value2 = nstate.getpixel(xy2)
    nstate.putpixel(xy1, value2)
    nstate.putpixel(xy2, value1)
    
    # Calculate the new energy
    nenergy = energy
    nenergy -= (pixel_energy(xy1, state) + pixel_energy(xy2, state)) * 2
    nenergy += (pixel_energy(xy1, nstate) + pixel_energy(xy2, nstate)) * 2
    
    return (nstate, nenergy)


def p_move(e, enew, temp):
    if enew < e:
        return 1.0
    
    # Simple, but works just by itself:
    prob = temp/INITIAL_TEMP
    
    # Penalize large energy increases:
    diff = enew - e
    prob *= math.exp(-3.0 * diff / temp)

    return prob


# TODO: adaptive simulated annealing, ie. adjust the cooling schedule dynamically
def cool(temp):
    count = 0
    while temp > 0:
        yield temp
        count += 1
        temp -= TEMP_MOD
    print("Cooling complete. Number of iterations: " + str(count))


def randompixel():
    #def rint():
    #    return random.randint(0, 255)
    #return (rint(), rint(), rint())
    return random.choice([(255, 255, 0), (255, 0, 0),
                          (255, 160, 255), (0, 0, 0)])


def main():
    schedule = cool(INITIAL_TEMP)
    
    # Create a black image
    initial_state = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))
    
    # Initialize the image
    for xy in pixels():
        initial_state.putpixel(xy, randompixel())
    initial_state.save('original.png')
   
    final_state = sanneal.find_minimum(initial_state, schedule,
                                       get_energy, get_neighbor, p_move)

    final_state.save('final.png')


if __name__ == '__main__':
    #cProfile.run('main()')
    main()
