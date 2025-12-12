import helpers.load_input as li
import time
import heapq


def main(better_data):
    count = 0
    shapes = {0:7,1:5,2:7,3:6,4:7,5:7}
    for line in better_data:
        print(line)
        area = int(line[0].split("x")[0]) * int(line[0].split("x")[1])
        packages = line[1]
        naive_required_area = 0
        for index,package in enumerate(packages):
            naive_required_area += package * shapes[index]
        if naive_required_area > area:
            print("0")
            continue
        else:
            count += 1
    print("Acceptable packages in total areas:", count)

if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("12")
    #data = li.load_input("12test")
    
    
    better_data = []
    for line in data:
        print(line)
        if line.endswith(":"):
            continue
        if line.startswith("#") or (line.strip() == "") or (line.startswith(".")):
            continue
        line = line.strip()
        splitline = line.strip().split(" ")
        area = splitline[0].replace(":", "")
        packages = []
        for item in splitline[1:]:
            packages.append(int(item))
        better_data.append([area, packages])
    main(better_data)
        
    
    end_time = time.time()