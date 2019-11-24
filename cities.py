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
  
def print_cities(road_map):
    for i in range(0, len(road_map)):
        print(road_map[i][1]+" "+str(round(road_map[i][2],2))+" "+str(round(road_map[i][3],2)))
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    pass

def compute_total_distance(road_map):
    #sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
    import math
    distance = 0

    for i in range(0,len(road_map)-1):
        x = (road_map[i][2] - road_map[i+1][2])**2
        y = (road_map[i][3] - road_map[i+1][3])**2
        distance += math.sqrt(x+y)

    x_last = (road_map[len(road_map)-1][2] - road_map[0][2])**2
    y_last = (road_map[len(road_map)-1][3] - road_map[0][3])**2

    last_distance = math.sqrt(x_last+y_last)

    total_distance = distance + last_distance

    return total_distance #-999999
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """

def swap_cities(road_map, index1, index2):
    new_road_map = road_map
    for i in range(len(new_road_map)):
        if new_road_map[i][1] == index1:
            a = new_road_map[i]
            print(a)
        elif new_road_map[i][1] == index2:
            b = new_road_map[i]
            print(b)

    for i in range(len(new_road_map)):
        if new_road_map[i][1] == index1:
            new_road_map[i] = b
        elif new_road_map[i][1] == index2:
            new_road_map[i] = a

    # WHAT HAPPENS IF INDEX 1 = INDEX 2

    return (new_road_map, compute_total_distance(new_road_map)) # ([('Nonesense_State', 'Nonesense__City', 999999.999999, 999999.999999)])
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def shift_cities(road_map):
    return ([('Nonesense_State', 'Nonesense__City', 999999.999999, 999999.999999)])
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """

def find_best_cycle(road_map):
    return 1
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    return 1
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    return 1
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
    road_map = read_cities('city-data.txt')
    total_distance = compute_total_distance(road_map)
    print(total_distance)
    swapped = swap_cities(road_map, 'Montgomery', 'Montgomery')
    print(swapped)



