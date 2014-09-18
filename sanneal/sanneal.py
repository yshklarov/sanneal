import random


# find_minimum: Finds the minimum value by simulated annealing.
#   state: the initial state
#   cooling_schedule: a generator which yields successive temperatures, for
#       example: range(100,0,-1)
#   energy: a function which takes a state as its argument, and returns energy
#       of that state
#   next_neighbor: a function which takes a state as input and returns a tuple
#       of a random neighboring state and its energy
#   p_move: a function of three variables: the old energy, the new energy, and
#       the current temperature. Should return the probability of moving to the
#       new energy at that temperature, as a value between 0 and 1.
def find_minimum(state, cooling_schedule, get_energy, next_neighbor, p_move):
    energy = get_energy(state)
    einit = energy
    
    for temp in cooling_schedule:
        (snew, enew) = next_neighbor(state, energy)
        if random.uniform(0, 1) < p_move(energy, enew, temp):
            (state, energy) = (snew, enew)
            print("Temperature: " + str(temp))
            print("Energy: " + str(energy))
    
    #print("Final energy (incremental calculation):" + str(energy))
    #print("Initial energy: " + str(einit))
    #print("Minimum state is " + str(state) + " with energy " +
    #      str(get_energy(state)) + ".")
    
    return state
