from . import sanneal
import math
import random
import csv

INITIAL_TEMP = 100


def get_dist_getter(distdict):
    
    def get_total_dist(itinerary):
        dist = 0
        for i in range(len(itinerary)-1):
            cfrom = itinerary[i]
            cto = itinerary[i+1]
            dist += distdict[cfrom, cto]
        return dist
        
    return get_total_dist


def get_neighbor_getter(energy_of):
    # Returns a 2-tuple: a random neighboring state and its energy.
    def get_neighbor(state, energy):
        length = len(state)
        newstate = state.copy()
        
        # Reverse a random consecutive sequence
        seq_len = random.randint(2, length-1)
        i = random.randint(0, length - seq_len)
        newstate[i:i+seq_len] = reversed(newstate[i:i+seq_len])
        
        return (newstate, energy_of(newstate))
    
    return get_neighbor


def p_move(e, enew, temp):
    if enew < e:
        return 1.0
    
    # Simple, but works just by itself:
    prob = temp/INITIAL_TEMP
    
    # Penalize large energy increases:
    #diff = enew - e
    #prob *= math.exp(- diff / temp)

    return prob


# TODO: adaptive simulated annealing, ie. adjust the cooling schedule dynamically
def temperature():
    temp = INITIAL_TEMP
    count = 0
    while temp > 0:
        yield temp
        count += 1
        temp = temp * 0.99995 - 1e-11
    print("Cooling complete. Number of iterations: " + str(count))


def main():
    print('Let''s visit all the capitals! Calculating fastest route.')
    
    with open('sanneal/capdist.csv', newline='') as csvfile:
        capreader = csv.DictReader(csvfile, delimiter=',')
        distances = {}
        for row in capreader:
            # (country 1, country 2): distance in km
            distances[(row['ida'], row['idb'])] = int(row['kmdist'])

    with open('sanneal/capabbrevs.dat', newline='', encoding='utf-8') as csvfile:
        abbrreader = csv.reader(csvfile, delimiter='|')
        names = {}
        for row in abbrreader:
            # country abbreviation: full name
            names[row[0]] = row[1]

    dist_getter = get_dist_getter(distances)
    
    # Get a list of unique countries
    initial_itinerary = list(set(country for (country, _) in distances))
    initial_itinerary.sort()
    pretty = [names[abbr] for abbr in initial_itinerary]
    print('Countries: ' + ', '.join(pretty) + '.')
    print('Total distance: ' + str(dist_getter(initial_itinerary)) + ' km.')
    
    final_itinerary = sanneal.find_minimum(initial_itinerary,
            temperature(), dist_getter, get_neighbor_getter(dist_getter), p_move)
    
    pretty = [names[abbr] for abbr in final_itinerary]
    print('Itinerary: ' + ', '.join(pretty) + '.')
    print('Total distance: ' + str(dist_getter(final_itinerary)) + ' km.')


if __name__ == '__main__':
    main()
