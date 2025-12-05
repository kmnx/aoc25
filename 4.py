import helpers.load_input as li
import copy


def position_check(array, movable_rolls):
    new_map = [[0] * len(array[0]) for i in range(len(array))]
    for x, line in enumerate(array):
        for y, char in enumerate(line):
            # print("we're at:", x, y, "with", array[x][y])
            if char == "@":
                position_count = 0
                for a in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]:
                    if (
                        (x + a[0] < 0)
                        or (y + a[1] < 0)
                        or (x + a[0] == len(array[0]))
                        or (y + a[1] == len(array))
                    ):
                        pass
                    else:
                        # print("testing: ", x + a[0], y + a[1])
                        if array[x + a[0]][y + a[1]] == "@":
                            position_count += 1
                if position_count < 4:
                    movable_rolls.append((x, y))
                    new_map[x][y] = "."
                else:
                    new_map[x][y] = array[x][y]
            else:
                new_map[x][y] = array[x][y]
    return movable_rolls, new_map


if __name__ == "__main__":
    # data = li.load_input("input4test")
    data = li.load_input("input4")

    reference = copy.deepcopy(data)
    movable_rolls = []

    # for line in data:
    #    print(line)
    movable, new = position_check(data, movable_rolls)
    print("Part 1:")
    print(len(movable_rolls))

    movable_rolls = []
    unchanged = False
    while unchanged == False:
        movable, new = position_check(data, movable_rolls)
        if new == data:
            unchanged = True
        else:
            data = copy.deepcopy(new)

    print("Part 2:")
    print(len(movable_rolls))
