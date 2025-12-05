import helpers.load_input as li
import copy
import time


def range_maker(raw_ranges):
    print("len raw ranges", len(raw_ranges))
    better_ranges = []
    for line in raw_ranges:
        processed = False
        splitrange = line
        print("new range", splitrange)
        for existing_range in better_ranges:
            print("currently tested range: ", existing_range)
            # completely in existing range
            if (
                splitrange[0] >= existing_range[0]
                and splitrange[1] <= existing_range[1]
            ):
                processed = True

            # completely contains existing range
            elif (splitrange[0] <= existing_range[0]) and (
                splitrange[1] >= existing_range[1]
            ):
                existing_range[0] = splitrange[0]
                existing_range[1] = splitrange[1]
                processed = True
            # starts earlier, end is in range
            elif (
                splitrange[0] < existing_range[0]
                and splitrange[1] >= existing_range[0]
                and splitrange[1] <= existing_range[1]
            ):
                existing_range[0] = splitrange[0]
                processed = True
            # start is in existing range, ends later
            elif (
                splitrange[0] >= existing_range[0]
                and splitrange[0] <= existing_range[1]
                and splitrange[1] > existing_range[1]
            ):
                existing_range[1] = splitrange[1]
                processed = True
        if processed == False:
            better_ranges.append(splitrange)
    print(better_ranges)
    print(len(better_ranges))
    return better_ranges


def main(data):
    print(data)
    raw_ranges = []
    ingredients = []
    for line in data:
        if "-" in line:
            splits = line.split("-")
            raw_ranges.append([int(splits[0]), int(splits[1])])
        elif line == "":
            pass
        else:
            ingredients.append(line)

    unchanged = False
    previous_ranges = []
    while unchanged == False:
        better_ranges = range_maker(raw_ranges)
        if better_ranges == previous_ranges:
            unchanged = True
        else:
            previous_ranges = copy.deepcopy(better_ranges)
            raw_ranges = copy.deepcopy(better_ranges)
    print(better_ranges)

    fresh_count = 0
    for ingredient in ingredients:
        spoiled = True
        for range in better_ranges:
            if int(ingredient) >= range[0] and int(ingredient) <= range[1]:
                spoiled = False
                break
        if spoiled == False:
            print(ingredient, "is fresh")
            fresh_count += 1
    print("Fresh Ingredients", fresh_count)

    fresh_range_count = 0
    for range in better_ranges:
        fresh_range_count += (range[1] - range[0]) + 1
    print("Fresh IDs", fresh_range_count)


if __name__ == "__main__":
    start_time = time.time()
    # data = li.load_input("input5test")
    data = li.load_input("input5")
    main(data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")
