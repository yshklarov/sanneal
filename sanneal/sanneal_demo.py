from . import sanneal
from PIL import Image
import math
import random


# We will minimize f(x) = x*ln(x). The minimum should be f(0.368) ≈ 0.368.
MINSTATE = 0.0
MAXSTATE = 1.0
INITIAL_STATE = 0.5
INITIAL_TEMP = 1.0
NEIGHBOR_RADIUS = 0.1


def energy(state):
    return state * math.log(state)

def get_neighbor(state):
    return random.uniform(max(MINSTATE, state - NEIGHBOR_RADIUS),
                          min(MAXSTATE, state + NEIGHBOR_RADIUS))

def p_move(e, enew, temp):
    if enew < e:
        return 1.0
    
    # Simple, but works just by itself:
    prob = temp/INITIAL_TEMP
    
    # If we want to penalize large energy increases:
    diff = enew - e
    prob *= math.exp(-3.0 * diff / temp)

    return prob

# TODO: adapted simulated annealing, ie. adjust the cooling schedule dynamically
def cool(temp):
    count = 0
    while temp > 0:
        yield temp
        count += 1
        temp = temp * 0.9 - 0.0000001
    print("Cooling complete. Number of iterations: " + str(count))

def main():
    schedule = cool(INITIAL_STATE)
    final_state = sanneal.find_minimum(INITIAL_STATE, schedule,
                                       energy, get_neighbor, p_move)
    print("Minimum state is " + str(final_state) + " with energy " +
          str(energy(final_state)) + ".")


if __name__ == '__main__':
    main()
