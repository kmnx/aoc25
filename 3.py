import helpers.load_input as li

data = li.load_input("input3")

# data = ["987654321111111","811111111111119","234234234234278","818181911112111"]


def array_cutter(in_array):
    for index, num in enumerate(in_array):
        # we're at the end and no previous number was bigger so we can safely delete
        if index == len(in_array) - 1:
            del in_array[index]
            return in_array
        # next number is bigger so we should delete the current one
        elif num < in_array[index + 1]:
            del in_array[index]
            return in_array


sum = 0
for line in data:
    in_array = [int(c) for c in line]
    while len(in_array) > 2:
        in_array = array_cutter(in_array)
    final_string = ""
    for n in in_array:
        final_string = final_string + str(n)
    final_num = int(final_string)

    # print(final_num)
    sum += final_num
print("Part 1:")
print(sum)
sum = 0
for line in data:
    in_array = [int(c) for c in line]
    while len(in_array) > 12:
        in_array = array_cutter(in_array)
    final_string = ""
    for n in in_array:
        final_string = final_string + str(n)
    final_num = int(final_string)

    # print(final_num)
    sum += final_num
print("Part 2:")
print(sum)
# 169077317650774
