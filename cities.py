import math
import random
import copy

def read_cities(file_name):
    infile = open(file_name, 'r')

    with infile:
        road_in = [x.strip().split('\t') for x in infile]

    for i in range(0,len(road_in)):
        road_in[i][2] = float(road_in[i][2])
        road_in[i][3] = float(road_in[i][3])

    road_map = []
    for i in range(0,len(road_in)):
        road_map.append(tuple(road_in[i]))

    infile.close()

    return road_map
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    pass
  
def compute_total_distance(road_map):
    #sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
    distance = 0

    for i in range(0,len(road_map)-1):
        x = (road_map[i][2] - road_map[i+1][2])**2
        y = (road_map[i][3] - road_map[i+1][3])**2
        distance += math.sqrt(x+y)

    x_last = (road_map[len(road_map)-1][2] - road_map[0][2])**2
    y_last = (road_map[len(road_map)-1][3] - road_map[0][3])**2

    last_distance = math.sqrt(x_last+y_last)

    total_distance = distance + last_distance

    return total_distance
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """

def print_cities(road_map):
    print(str('CITY').ljust(20)+str('LATITUDE').ljust(10)+str('LONGITUDE').ljust(10))
    for i in range(0, len(road_map)):
        print(str(road_map[i][1]).ljust(20)+str(round(road_map[i][2],2)).ljust(10)+str(round(road_map[i][3],2)).ljust(10))
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    pass

def swap_cities(road_map, index1, index2):
    if index1 == index2:
        return (road_map, compute_total_distance(road_map))

    for i in range(len(road_map)):
        if road_map[i][1] == index1:
            a = road_map[i]
        elif road_map[i][1] == index2:
            b = road_map[i]

    for i in range(len(road_map)):
        if road_map[i][1] == index1:
            road_map[i] = b
        elif road_map[i][1] == index2:
            road_map[i] = a

    return (road_map, compute_total_distance(road_map))
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def shift_cities(road_map):
    new_map = [road_map[-1]]
    new_map.extend(road_map)
    new_map.pop(-1)
    for i in range(len(road_map)):
        road_map[i] = new_map[i]
    return road_map

    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """

def find_best_cycle(road_map):

    counter = 0
    best_distance = compute_total_distance(road_map)
    best_map = road_map
    while counter <= 10000:
        new_map1 = shift_cities(road_map)
        num1 = round((len(new_map1) - 1) * random.random())
        num2 = round((len(new_map1) - 1) * random.random())
        new_map2 = swap_cities(new_map1, new_map1[num1][1], new_map1[num2][1])
        if new_map2[1] < best_distance:
            best_distance = new_map2[1]
            best_map = copy.copy(new_map2[0])
        else:
            road_map = copy.copy(best_map)
        counter += 1

    return (best_map, best_distance)

    #counter = 0
    #continue_map = road_map
    #best_map = road_map
    #print("FIRST best map", best_map)
    #best_distance = compute_total_distance(road_map)
    #while counter <= 20:
    #    new_map1 = shift_cities(continue_map)
    #    num1 = round((len(new_map1) - 1) * random.random())
    #    num2 = round((len(new_map1) - 1) * random.random())
    #    new_map2 = swap_cities(new_map1, new_map1[num1][1], new_map1[num2][1])
    #    print(new_map2)
    #    check_distance = new_map2[1]
    #    print("Check dist:", check_distance)
    #    print("Check best dist:", best_distance)
    #    if float(check_distance) < float(best_distance):
    #        best_distance = check_distance
    #        best_map = new_map2[0]
    #        print("Best_Map: ", best_map)
    #        print("Best Dist: ", best_distance)
    #        continue_map = new_map2[0]
    #    else:
    #        continue_map = new_map2[0]
    #        print("Best_Map2: ", best_map)
    #    counter += 1

    #print(best_map)
    #print(compute_total_distance(best_map))
    #print(best_distance)

    #return (best_map, compute_total_distance(best_map))
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):

    for i in range(0, len(road_map[0])-1):
        x = (road_map[0][i][2] - road_map[0][i+1][2])**2
        y = (road_map[0][i][3] - road_map[0][i+1][3])**2
        dist = round(math.sqrt(x + y),2)
        print(str(i).ljust(3)+". "+road_map[0][i][1].ljust(20)+"-->".ljust(10)+\
              str(i+1).ljust(3)+". "+road_map[0][i+1][1].ljust(20)+"Cost: "+str(dist))

    x = (road_map[0][len(road_map[0])-1][2] - road_map[0][0][2])**2
    y = (road_map[0][len(road_map[0])-1][3] - road_map[0][0][3])**2
    dist = round(math.sqrt(x + y),2)
    print(str(len(road_map[0])-1).ljust(3) + ". " + road_map[0][len(road_map[0])-1][1].ljust(20) + "-->".ljust(10) + \
          str(0).ljust(3) + ". " + road_map[0][0][1].ljust(20) + "Cost: " + str(dist))

    print()
    print("Total Cost: ", str(round(road_map[1],2)))

    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def visualise(road_map):

    x = []
    for v in range(0, len(road_map)):
        x.append(road_map[v][2])
    y = []
    for w in range(0, len(road_map)):
        y.append(road_map[w][3])

    # Dynamically set boundaries for map and extend by 1 to ensure nothing out of bounds from rounding
    x_max = round(max(x) + 1)
    x_min = round(min(x) - 1)
    y_max = round(max(y) + 1)
    y_min = round(min(y) - 1)

    print(str('').ljust(5), end='')
    for s in range(y_min, y_max, 1):
        print(str(s).ljust(4), end=" ")

    print()
    for i in range(x_min, x_max, 1):
        print(str(i).ljust(4), end='  ')
        for j in range(y_min, y_max, 1):
            for k in range(0, len(road_map)):
                if i == round((road_map[k][2])) and j == round((road_map[k][3])):
                    print(str(k).ljust(3), end="  ")
                    break
            else:
                print(str('.').ljust(3), end="  ")
        print()

def main():
    try:
        road_map = read_cities('city-data.txt')
    except OSError:
        print('Could not open/read file - check file name is "city-data.txt" and data saved in same directory as cities.py')
        exit()
    starting_distance = round(compute_total_distance(road_map),2)
    print('### STARTING ROAD MAP ###')
    print('-------------------------')
    print_cities(road_map)
    print('')
    print('### STARTING DISTANCE ###')
    print('-------------------------')
    print(starting_distance)
    print('')
    best = find_best_cycle(road_map)
    print('### BEST CYCLE & DISTANCE ###')
    print('-----------------------------')
    print_map(best)
    print('-----------------------------------------------------------------------------')
    print('### VISUALISATION (VERTICAL AXIS = LATITUDE, HORIZONTAL AXIS = LONGITUDE) ###')
    print('###                  ^ Key for cities displayed above ^                   ###')
    print('-----------------------------------------------------------------------------')
    visualise(best[0])

    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__":
    main()
