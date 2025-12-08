import helpers.load_input as li

data = li.load_input("input2")

# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(",")
data = data[0].split(",")
# print(data)

data_list = []
for line in data:
    # print(line)
    parts = line.split("-")
    start = int(parts[0])
    end = int(parts[1])
    data_list.append((start, end))

# print(data_list)

summed = 0
for ids in data_list:
    # print(ids)
    start = ids[0]
    end = ids[1]
    for num in range(start, end + 1):
        # print(num)
        split_id_start = str(num)[0 : len(str(num)) // 2]
        split_id_end = str(num)[len(str(num)) // 2 :]
        # print(split_id_start)
        # print(split_id_end)
        if not split_id_end.startswith("0") and not split_id_start.startswith("0"):
            if split_id_start == split_id_end:
                # print("found one!")
                # print(num)
                summed += num

print("part 1:")
print(summed)

summed = 0
for ids in data_list:
    # print(ids)
    start = ids[0]
    end = ids[1]
    for num in range(start, end + 1):
        if num == 824824821:
            print("debug")
        # print(num)
        # print(len(str(num)))
        if len(str(num)) > 1:
            if len(str(num)) % 2 == 0:
                if str(num)[0 : len(str(num)) // 2] == str(num)[len(str(num)) // 2 :]:
                    summed += int(num)
                    # print("found one!")
                    # print(num)
                    continue
            if len(str(num)) % 3 == 0:
                if str(num)[0:3] == str(num)[3:6] == str(num)[6:9]:
                    summed += int(num)
                    # print("found one!")
                    # print(num)
                    continue
                elif str(num)[0:2] == str(num)[2:4] == str(num)[4:6]:
                    summed += int(num)
                    # print("found one!")
                    # print(num)
                    continue
            if len(str(num)) % 5 == 0:
                if (
                    str(num)[0:2]
                    == str(num)[2:4]
                    == str(num)[4:6]
                    == str(num)[6:8]
                    == str(num)[8:10]
                ):
                    summed += int(num)
                    # print("found one!")
                    # print(num)
                    continue
            # primes:
            if len(set(str(num))) == 1:
                # print("found one!")
                # print(num)
                summed += int(num)
                continue
print("part 2:")
print(summed)
