import helpers.load_input as li
import time
import math
import heapq
from sympy import symbols, linsolve, solve, Eq, Integer, Matrix
import itertools

def minimize_solution_sum(general_solution):
    solution_vec, params_vec = general_solution
    params = list(params_vec)
    min_sum = None
    best_values = None
    best_solution = None

    # Extract bounds for each parameter from solution lines with <=1 parameter
    param_bounds = {param: [0, 100] for param in params}  # default bounds

    for expr in solution_vec:
        involved = [param for param in params if param in expr.free_symbols]
        if len(involved) == 1:
            param = involved[0]
            # Try to solve expr >= 0 for param
            bounds = solve(expr >= 0, param)
            # bounds may be a list of inequalities or values
            if isinstance(bounds, list):
                for b in bounds:
                    # Only handle simple inequalities
                    if hasattr(b, 'rel_op'):
                        if b.rel_op == '<=':
                            param_bounds[param][1] = min(param_bounds[param][1], int(b.rhs))
                        elif b.rel_op == '>=':
                            param_bounds[param][0] = max(param_bounds[param][0], int(b.rhs))
        elif len(involved) == 0:
            # If no parameter, just check if expr >= 0 is possible
            if expr < 0:
                return None  # No valid solution

    # Build search ranges from bounds
    search_ranges = [range(param_bounds[param][0], param_bounds[param][1] + 1) for param in params]

    # Try all combinations in reduced ranges
    for values in itertools.product(*search_ranges):
        subs = dict(zip(params, values))
        candidate = solution_vec.subs(subs)
        if all((c.is_integer and c >= 0) for c in candidate):
            total = sum([int(c) for c in candidate])
            if min_sum is None or total < min_sum:
                min_sum = total
                best_values = values
                best_solution = candidate

    print("Best parameter values:", dict(zip(params, best_values)))
    print("Best solution:", best_solution)
    print("Minimum sum:", min_sum)
    return min_sum


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
    joltages = state_array[2]

    initial_state = [False for i in range(len(target_state))]
    current_state = initial_state
    pushed_list = []
    heapqueue = []
    pushes = 0
    
    all_combos = all_button_combinations(len(buttons))
    #print(all_combos)
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

def print_2d_array(map):
    print("Map:")
    for line in map:
        tempstr = ""
        for c in line:
            tempstr += str(c) + " "
        print(tempstr)
    print("-----------")

def joltages_tester(state_array,o):
    print(" New Joltages Test Case ", o)
    buttons = state_array[1]
    # buttons = [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]], [3, 5, 4, 7]]
    joltages = state_array[2]
    # joltages = [32, 23, 39, 9]
    my_array = [[0 for i in range(len(buttons))] for j in range(len(joltages))]
    for i,button in enumerate(buttons):
        for number in button:
            my_array[number][i] = 1
    print_2d_array(my_array)
    print("Joltages to match:", joltages)
    A = Matrix(my_array)
    B = Matrix(joltages)
    try:
        solution = A.gauss_jordan_solve(B)
        print("Joltages solution found:", solution)
        min_sol = minimize_solution_sum(solution)
        
    except:
        print("No Joltages solution found")
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
        sum += joltages_tester(line,o)
    print("Sum of all joltages tests:", sum)
    

if __name__ == "__main__":
    start_time = time.time()
    data = li.load_input("10")
    #data = li.load_input("10test")
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
                item = item.replace("(","")
                item = item.replace(")","")
                split_string = item.split(",")
                for n in split_string:
                    switch_row.append(int(n))
                switches.append(switch_row)
            if item.startswith("{"):
                item = item.replace("{","")
                item = item.replace("}","")
                joltages = [int(n) for n in item.split(",")]

        better_data.append([lights,switches,joltages])
        # print(x,y,z)
    main(better_data)
    end_time = time.time()
    print("Execution Time:", end_time - start_time, "seconds")