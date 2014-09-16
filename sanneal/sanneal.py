import random


# find_minimum: Finds the minimum value by simulated annealing.
#   state: the initial state
#   cooling_schedule: a generator which yields successive temperatures, for
#       example: range(100,0,-1)
#   energy: a function which takes a state as its argument, and returns energy
#       of that state
#   next_neighbor: a function which takes a state as input and returns a random
#       neighboring state
#   p_move: a function of three variables: the old energy, the new energy, and
#       the current temperature. Should return the probability of moving to the
#       new energy at that temperature, as a value between 0 and 1.
def find_minimum(state, cooling_schedule, energy, next_neighbor, p_move):
    eold = energy(state)
    
    for temp in cooling_schedule:
        snew = next_neighbor(state)
        enew = energy(snew)
        if random.uniform(0, 1) < p_move(eold, enew, temp):
            state = snew
            eold = enew
    
    return state
