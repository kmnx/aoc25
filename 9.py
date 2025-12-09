import helpers.load_input as li
import time
import math
import itertools


def distance(p, q):
    distance = math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)
    return distance
def get_area(p,q):
    area = (abs(p[0]-q[0])+1)*(abs(p[1]-q[1])+1)
    return area
def print_2d_array(map):
    print("Map:")
    for line in map:
        tempstr = ""
        for c in line:
            tempstr += c
        print(tempstr)
    print("-----------")


def main(data):
    print(data)
    all_areas = []
    for line_pos, p in enumerate(data):
        for row in range(line_pos + 1, len(data)):
            # print(i,j)
            area = get_area(p, data[row])
            all_areas.append((area, [line_pos, row]))
    sorted_areas = sorted(all_areas, key=lambda x: x[0])
    print(sorted_areas)
    print(sorted_areas[-1])
    print(data[sorted_areas[-1][1][0]])
    print(data[sorted_areas[-1][1][1]])
    

    
    # find corners
    '''tl = data[0]
    tr = data[0]
    bl = data[0]
    br = data[0]
    for i,p in enumerate(data):
        if p[0] <= tl[0] and p[1] <= tl[1]:
            tl = p
        if p[0] >= tr[0] and p[1] <= tr[1]:
            tr = p
        if p[0] <= bl[0] and p[1] >= bl[1]:
            bl = p
        if p[0] >= br[0] and p[1] >= br[1]:
            br = p
    area1 = get_area(tl,br)
    area2 = get_area(tr,bl)
    print(area1,area2)'''
    map = []
    largest_col = 0
    largest_row = 0
    for p in data:
        if p[0] > largest_col:
            largest_col = p[0]
        if p[1] > largest_row:
            largest_row = p[1]
    map = [["." for x in range(largest_col+1)] for y in range(largest_row+1)]
    # [7,1] means map[1][7]
    for p in data:
        map[p[1]][p[0]] = "#"
    print_2d_array(map)
    # horizontal fill
    for line_pos,line in enumerate(map):
        first_red = 0
        last_red = 0
        for row,c in enumerate(line):
            if c == "#":
                if first_red == 0:
                    first_red = row
                else:
                    if last_red == 0  or last_red < row:
                        last_red = row
        if (first_red == last_red) or (first_red == 0) or (last_red == 0):
            pass
        else:
            for c in range(first_red,last_red):
                if line[c] == ".":
                    line[c] = "X"
        print_2d_array(map)
    # vertical fill
    for line_pos in range(len(map[0])):
        first_red = 0
        last_red = 0
        for row in range(len(map)):
            if map[row][line_pos] == "#":
                if first_red == 0:
                    first_red = row
                else:
                    if last_red == 0  or last_red < row:
                        last_red = row
        if (first_red == last_red) or (first_red == 0) or (last_red == 0):
            pass
        else:
            for c in range(first_red,last_red):
                if map[c][line_pos] == ".":
                    map[c][line_pos] = "X"
        print_2d_array(map)
    '''# horizontal fill green
    for line_pos,line in enumerate(map):
        first_red = 0
        last_red = 0
        for row,c in enumerate(line):
            if c in ["#","X"]:
                if first_red == 0:
                    first_red = row
                else:
                    if (last_red == 0) or last_red < row:
                        last_red = row
        if (first_red == last_red) or (first_red == 0) or (last_red == 0):
            pass
        else:
            for c in range(first_red,last_red):
                if line[c] == ".":
                    line[c] = "X"
            print_2d_array(map)'''
            
        



    






if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("9test")
    data = li.load_input("9")
    better_data = []
    for i, line in enumerate(data):
        x, y = line.split(",")
        # print(x,y,z)
        better_data.append([int(x), int(y)])
    main(better_data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")
