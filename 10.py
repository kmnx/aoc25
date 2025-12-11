import helpers.load_input as li
import time
import heapq
from z3 import Ints, Solver, Sum, sat


def minimize_solution_sum_z3(A, b):
    n_vars = len(A[0])
    x = [Ints(f"x{i}")[0] for i in range(n_vars)]
    s = Solver()
    # all variables must be >= 0
    for var in x:
        s.add(var >= 0)
    # add linear constraints: Ax = b
    for row, rhs in zip(A, b):
        s.add(Sum([coef * var for coef, var in zip(row, x)]) == rhs)
    # objective: minimize sum(x)
    min_sum = None
    best_sol = None
    # iteratively search for better solutions
    while True:
        if s.check() == sat:
            m = s.model()
            sol = [m[var].as_long() for var in x]
            total = sum(sol)
            if min_sum is None or total < min_sum:
                min_sum = total
                best_sol = sol
                # add constraint for a better solution next time
                s.add(Sum(x) < min_sum)
        else:
            break
    if best_sol is not None:
        return min_sum
    else:
        print("No integer solution found.")
        return None


def backtrack_combos(n, start, path, combos):
    if path:
        combos.append(path[:])
    for i in range(start, n):
        path.append(i)
        backtrack_combos(n, i + 1, path, combos)
        path.pop()


def all_button_combinations(n):
    combos = []
    backtrack_combos(n, 0, [], combos)
    return combos


def button_masher(state_array):
    target_state = state_array[0]
    buttons = state_array[1]
    initial_state = [False for i in range(len(target_state))]
    current_state = initial_state
    heapqueue = []
    pushes = 0

    all_combos = all_button_combinations(len(buttons))
    # print(all_combos)
    for combo in all_combos:
        current_state = initial_state[:]
        pushes = 0
        for button_index in combo:
            button = buttons[button_index]
            for light_index in button:
                current_state[light_index] = not current_state[light_index]
            pushes += 1
        if current_state == target_state:
            heapq.heappush(heapqueue, (pushes, combo))

    if heapqueue:
        best = heapq.heappop(heapqueue)
        print("Best solution found with", best[0], "pushes:", best[1])
        return int(best[0])
    else:
        print("No solution found")
        return None


def joltages_tester(state_array, o):
    # print(" New Joltages Test Case ", o)
    buttons = state_array[1]
    joltages = state_array[2]
    my_array = [[0 for i in range(len(buttons))] for j in range(len(joltages))]
    for i, button in enumerate(buttons):
        for number in button:
            my_array[number][i] = 1

    min_sol = minimize_solution_sum_z3(my_array, joltages)
    return min_sol


def main(data):
    sum = 0
    for line in data:
        print(line)
        sum += button_masher(line)
    print("Sum of all button presses:", sum)
    sum = 0
    o = 0
    for line in data:
        o += 1
        sum += joltages_tester(line, o)
        # print("line was:", o, "current sum:", sum)
    print("Sum of all joltages tests:", sum)


if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("10")
    # data = li.load_input("10test")
    better_data = []
    for line in data:
        lights = []
        switches = []
        joltages = []
        unsorted = line.split(" ")
        for item in unsorted:
            if item.startswith("["):
                for c in item:
                    if c == ".":
                        lights.append(False)
                    elif c == "#":
                        lights.append(True)
            if item.startswith("("):
                switch_row = []
                item = item.replace("(", "")
                item = item.replace(")", "")
                split_string = item.split(",")
                for n in split_string:
                    switch_row.append(int(n))
                switches.append(switch_row)
            if item.startswith("{"):
                item = item.replace("{", "")
                item = item.replace("}", "")
                joltages = [int(n) for n in item.split(",")]

        better_data.append([lights, switches, joltages])
        # print(x,y,z)
    main(better_data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")
