import helpers.load_input as li
import time
import heapq
from z3 import Ints, Solver, Sum, sat

nodes = {}
class Node():
    def __init__(self,name):
        self.name = name
        self.connections = []


def find_paths(start, end):
    # Path found
    if start == end:
        return [[start]]
    # Dead end
    if not start.connections:
        return []
    paths = []
    # Check node's neighbors recursively
    for neighbor in start.connections:
        subpaths = find_paths(neighbor, end)
        for path in subpaths:
            paths.append([start] + path)
    return paths

def main(better_data):
    for line in better_data:
        _from = line[0]
        _to = line[1]
        if _from not in nodes:
            nodes[_from] = Node(_from)
        # Create destination nodes if not exist
        for device in _to:
            if device not in nodes:
                nodes[device] = Node(device)
            # Link nodes
            nodes[_from].connections.append(nodes[device])


    print("hey")

memo = {}

def count_paths(node, end, has_fft, has_dac):
    # Check if we already computed this
    memo_key = (node.name, has_fft, has_dac)
    if memo_key in memo:
        return memo[memo_key]
    # Update flags if we're at a required node
    if node.name == 'fft':
        has_fft = True
    if node.name == 'dac':
        has_dac = True
    # Path found
    if node == end:
        # Void paths without both flags
        result = 1 if has_fft and has_dac else 0
        # Update memo
        memo[memo_key] = result
        return result
    # Dead end
    if not node.connections:
        # Update memo
        memo[memo_key] = 0
        return 0
    # Sum paths
    count = 0
    for neighbor in node.connections:
        count += count_paths(neighbor, end, has_fft, has_dac)
    memo[memo_key] = count
    return count

def main_two(better_data):
    

    memo = {}

if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("11")
    #data = li.load_input("11test")
    better_data = []
    for line in data:
        print(line)
        splitline = line.strip().split(":")
        in_node = splitline[0]
        out_nodes = splitline[1].strip().split(" ")
        better_data.append([in_node,out_nodes])
    main(better_data)
    answerp1 = len(find_paths(nodes['you'], nodes['out']))
    print("Part One Answer:", answerp1)

    part_two_test = ["svr: aaa bbb",
                        "aaa: fft",
                        "fft: ccc",
                        "bbb: tty",
                        "tty: ccc",
                        "ccc: ddd eee",
                        "ddd: hub",
                        "hub: fff",
                        "eee: dac",
                        "dac: fff",
                        "fff: ggg hhh",
                        "ggg: out",
                        "hhh: out"]
    better_data = []
    for line in data:
        #print(line)
        splitline = line.strip().split(":")
        in_node = splitline[0]
        out_nodes = splitline[1].strip().split(" ")
        better_data.append([in_node,out_nodes])
    print(better_data)
    sumtwo = count_paths(nodes['svr'], nodes['out'], False, False)
    print("Part Two Answer:", sumtwo)
    end_time = time.time()