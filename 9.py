import helpers.load_input as li
import time
import math


def get_area(p, q):
    area = (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)
    return area


# red herring, trying to even create the array leads to OOM for the real input
def print_2d_array(map):
    print("Map:")
    for line in map:
        tempstr = ""
        for c in line:
            tempstr += str(c)
        print(tempstr)
    print("-----------")


def main(data):
    # print(data)
    all_areas = []
    main_set = set()
    for tupel in data:
        main_set.add((tupel[0], tupel[1]))
    # brute force all combinations for part 1
    for line_pos, p in enumerate(data):
        for row in range(line_pos + 1, len(data)):
            # print(i,j)
            area = get_area(p, data[row])
            all_areas.append((area, [line_pos, row]))

    sorted_areas = sorted(all_areas, key=lambda x: x[0], reverse=True)
    print("Part 1:", sorted_areas[0])
    # 4745816424
    map = []
    largest_col = 0
    largest_row = 0
    for p in data:
        # print("Pass 1 point:",p)
        if p[0] > largest_col:
            largest_col = p[0]
        if p[1] > largest_row:
            largest_row = p[1]

    count = 0
    checked_set = set()
    boundary_set = set()
    # find all boundary points
    for pair in main_set:
        checked_set.add(pair)
        for other_pair in main_set:
            if other_pair in checked_set:
                pass

            elif pair == other_pair:
                # print("same pair")
                pass

            elif pair[0] == other_pair[0]:
                # print("found a line")
                # print(pair,other_pair)
                count += 1
                # print(count)
                for y in range(
                    min(pair[1], other_pair[1]), max(pair[1], other_pair[1]) + 1
                ):
                    boundary_set.add((pair[0], y))

            elif pair[1] == other_pair[1]:
                # print("found a line")
                # print(pair,other_pair)
                count += 1
                # print(count)
                for x in range(
                    min(pair[0], other_pair[0]), max(pair[0], other_pair[0]) + 1
                ):
                    boundary_set.add((x, pair[1]))

    # print("Size of boundary set:",len(boundary_set))
    # go through sorted areas from part 1 and find the first valid one
    for line in sorted_areas:
        # print(line)
        # print(data[line[1][0]],data[line[1][1]])
        # find corners of the two points
        p1 = data[line[1][0]]
        p2 = data[line[1][1]]
        tl = (min(p1[0], p2[0]), min(p1[1], p2[1]))
        br = (max(p1[0], p2[0]), max(p1[1], p2[1]))
        corners = [tl, br]
        all_corners_valid = True
        # if a boundary point is inside the rectangle, the rectangle must be invalid
        for bp in boundary_set:
            if bp[0] > tl[0] and bp[0] < br[0] and bp[1] > tl[1] and bp[1] < br[1]:
                all_corners_valid = False
                break
        if all_corners_valid:
            print("Found valid area:", line[0], tl, br)
            break


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
