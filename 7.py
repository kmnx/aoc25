import helpers.load_input as li
import time


def main(data):
    print(data)
    grand_array = []
    for line in data:
        line_array = []
        for c in line:
            line_array.append([c, 0])
        grand_array.append(line_array)

    splitter_locations = []
    unchecked_beam_positions = []
    checked_beam_positions = []
    for start_index, c in enumerate(grand_array[0]):
        if c[0] == "S":
            unchecked_beam_positions.append((0, start_index))
            grand_array[1][start_index][1] = 1
            grand_array[1][start_index][0] = "|"
            break
    out_positions = []
    splitter_locations = []
    while len(unchecked_beam_positions) > 0:
        check_this = unchecked_beam_positions.pop(0)
        checked_beam_positions.append(check_this)

        if check_this[0] + 1 == len(grand_array):
            # reached the end
            out_positions.append(check_this)
        elif grand_array[check_this[0] + 1][check_this[1]][0] == "^":
            if ((check_this[0] + 1, check_this[1])) not in splitter_locations:
                splitter_locations.append((check_this[0] + 1, check_this[1]))
            # left side:
            if check_this[1] - 1 > -1:
                if (
                    check_this[0] + 1,
                    check_this[1] - 1,
                ) not in unchecked_beam_positions:
                    unchecked_beam_positions.append(
                        (check_this[0] + 1, check_this[1] - 1)
                    )
                grand_array[check_this[0] + 1][check_this[1] - 1][1] += grand_array[
                    check_this[0]
                ][check_this[1]][1]
                grand_array[check_this[0] + 1][check_this[1] - 1][0] = "|"
            # right side:
            if check_this[1] + 1 < len(grand_array[0]):
                if (
                    check_this[0] + 1,
                    check_this[1] + 1,
                ) not in unchecked_beam_positions:
                    unchecked_beam_positions.append(
                        (check_this[0] + 1, check_this[1] + 1)
                    )
                grand_array[check_this[0] + 1][check_this[1] + 1][1] += grand_array[
                    check_this[0]
                ][check_this[1]][1]
                grand_array[check_this[0] + 1][check_this[1] + 1][0] = "|"
        elif grand_array[check_this[0] + 1][check_this[1]][0] == ".":
            if (check_this[0] + 1, check_this[1]) not in unchecked_beam_positions:
                unchecked_beam_positions.append((check_this[0] + 1, check_this[1]))
            grand_array[check_this[0] + 1][check_this[1]][1] += grand_array[
                check_this[0]
            ][check_this[1]][1]
            grand_array[check_this[0] + 1][check_this[1]][0] = "|"
        elif grand_array[check_this[0] + 1][check_this[1]][0] == "|":
            if (check_this[0] + 1, check_this[1]) not in unchecked_beam_positions:
                unchecked_beam_positions.append((check_this[0] + 1, check_this[1]))
            grand_array[check_this[0] + 1][check_this[1]][1] += grand_array[
                check_this[0]
            ][check_this[1]][1]

    out_count = 0
    for c in grand_array[-1]:
        if c == "|":
            out_count += 1
    print("out count:", out_count)

    for line in grand_array:
        temp_str = ""
        for pair in line:
            temp_str += pair[0]
        print(temp_str)

    for line in grand_array:
        temp_str = ""
        for pair in line:
            temp_str += f"{pair[0]}{pair[1]}"
        print(temp_str)
    sum_paths = 0
    for pair in grand_array[-1]:
        sum_paths += pair[1]

    print("splitters:", len(splitter_locations))
    print("Sum of paths:", sum_paths)


if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("input7")
    # data = li.load_input("input7test")

    main(data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")
