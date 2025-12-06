import helpers.load_input as li
import copy
import time


def main(data):
    all_items = []
    # print(data)
    for line in data:
        splitline = line.strip().split(" ")
        final_line = []
        for item in splitline:
            if item.strip() != "":
                final_line.append(item)

        if final_line != []:
            all_items.append(final_line)
    main_total = 0
    for i in range(len(all_items[0])):
        column_total = 0
        if all_items[-1][i] == "*":
            for j in range(len(all_items) - 1):
                if j == 0:
                    column_total = int(all_items[j][i])
                else:
                    column_total *= int(all_items[j][i])
        elif all_items[-1][i] == "+":
            for j in range(len(all_items) - 1):
                if j == 0:
                    column_total = int(all_items[j][i])
                else:
                    column_total += int(all_items[j][i])
        main_total += column_total
    print(main_total)

    grand_array = []
    grand_line = []
    for line in data:
        for c in line:
            grand_line.append(c)
        if line.strip() != "":
            grand_array.append(line)
    temp_one = ""
    transposed_array = []
    for i in range(len(grand_array[0])):
        for j in range(len(all_items) - 1):
            temp_one += grand_array[j][i]
        transposed_array.append(temp_one.strip())
        temp_one = ""
    ops = []
    for c in grand_array[-1]:
        if c == " ":
            pass
        else:
            ops.append(c)
    bundles = [[]]
    for item in transposed_array:
        if item == "":
            bundles.append([])
        else:
            bundles[-1].append(item)
    grand_total = 0
    for package in zip(ops, bundles):
        temp_sum = 0
        if package[0] == "*":
            for num in package[1]:
                if temp_sum == 0:
                    temp_sum = int(num)
                else:
                    temp_sum *= int(num)
            grand_total += temp_sum
        elif package[0] == "+":
            for num in package[1]:
                if temp_sum == 0:
                    temp_sum = int(num)
                else:
                    temp_sum += int(num)
            grand_total += temp_sum
    print(grand_total)


if __name__ == "__main__":
    start_time = time.time()
    # data = li.load_input("input6test")
    data = li.load_input("input6")
    main(data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")
