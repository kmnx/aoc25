import helpers.load_input as li

data = li.load_input("input1")

# print(data)


# data = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82',]
start = 50
zero_count = 0

for line in data:

    if line.startswith("L"):
        parts = line.split("L")
        num = int(parts[1])
        start -= num
        start = start % 100
        if start < 0:
            start += 100
        if start == 0:
            zero_count += 1
    elif line.startswith("R"):
        parts = line.split("R")
        num = int(parts[1])
        start += num
        start = start % 100
        if start < 0:
            start += 100
        if start == 0:
            zero_count += 1


print("part 1:")
print(zero_count)

start = 50
zero_count = 0
for line in data:
    # print("----"    )
    # print(start)
    # print(line)
    if line.startswith("L"):
        parts = line.split("L")
        num = int(parts[1])
        for _ in range(num):
            # print("decrementing")
            # print(start)
            start -= 1
            if start in [0]:
                # print("hit zero")
                zero_count += 1
            if start in [-100, 100]:
                start = 0
                zero_count += 1

    elif line.startswith("R"):
        parts = line.split("R")
        num = int(parts[1])
        for _ in range(num):
            start += 1
            if start in [0]:
                zero_count += 1
            if start in [-100, 100]:
                start = 0
                zero_count += 1
    # print(start)
    # print(zero_count)

print("part 2:")
print(zero_count)
