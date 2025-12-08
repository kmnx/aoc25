import helpers.load_input as li
import time
import math
import itertools


def distance(p, q):
    distance = math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)
    return distance


def main(data):
    # print(data)
    all_distances = []
    for i, p in enumerate(data):
        for j in range(i + 1, len(data)):
            # print(i,j)
            euc_dist = distance(p, data[j])
            all_distances.append((euc_dist, [i, j]))
    sorted_distances = sorted(all_distances, key=lambda x: x[0])
    # print(sorted_distances)
    # print(len(sorted_distances))
    seen = set()
    circuits = []
    connections_made = 0
    for line in sorted_distances:
        # print("conns made",connections_made)
        # print("seen",len(seen))
        if connections_made == 1000:
            sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
            a = len(sorted_circuits[0])
            b = len(sorted_circuits[1])
            c = len(sorted_circuits[2])
            print("Part 1, 1000 connections:", a, b, c, a * b * c)
        """if connections_made == 10:
            sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
            a = len(sorted_circuits[0])
            b = len(sorted_circuits[1])
            c = len(sorted_circuits[2])
            print("Part 1, 10 connections:", a, b, c, a * b * c)"""

        if line[1][0] not in seen and line[1][1] not in seen:
            seen.add(line[1][0])
            seen.add(line[1][1])
            # circuits.append([line[1][0], line[1][1]])
            circuits.append({line[1][0], line[1][1]})
            connections_made += 1

        elif line[1][0] in seen and line[1][1] not in seen:
            seen.add(line[1][1])
            for circuit in circuits:
                if line[1][0] in circuit:
                    circuit.add(line[1][1])
                    connections_made += 1

        elif line[1][1] in seen and line[1][0] not in seen:
            seen.add(line[1][0])
            for circuit in circuits:
                if line[1][1] in circuit:
                    circuit.add(line[1][0])
                    connections_made += 1

        elif line[1][0] in seen and line[1][1] in seen:
            c0 = None
            c1 = None
            for i, circuit in enumerate(circuits):
                if line[1][0] in circuit:
                    c0 = i
                if line[1][1] in circuit:
                    c1 = i
            if c0 == c1:
                connections_made += 1
            else:
                circuits[c0].update(circuits[c1])
                connections_made += 1
                del circuits[c1]
        """if len(seen) == 20 and len(circuits) == 1:
            dist = data[line[1][0]][0] * data[line[1][1]][0]
            print("Part 2 Distance, test data", dist)
            break"""

        if len(seen) == 1000 and len(circuits) == 1:
            dist = data[line[1][0]][0] * data[line[1][1]][0]
            print("Part 2 Distance", dist)
            break


if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("input8")
    # data = li.load_input("input8test")
    better_data = []
    for i, line in enumerate(data):
        x, y, z = line.split(",")
        # print(x,y,z)
        better_data.append([int(x), int(y), int(z)])
    main(better_data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")
