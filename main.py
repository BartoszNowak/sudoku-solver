import datetime

import example
import solution_generator

example_grid = example.get_grid()

cost = solution_generator.calculate_cost(example_grid)
print(example_grid)
print('Initial cost:', cost)

startTime = datetime.datetime.now()
min_cost = cost
best_grid = example_grid
take_first = False
epoch_count = 0
epoch_min_cost = min_cost
absolute_best_grid = example_grid
generation = 1
while True:
    children = None
    best_child_cost = None
    for i in range(0, 10):
        g = best_grid.copy()
        g = solution_generator.random_change(g)
        g = solution_generator.random_change(g)
        g = solution_generator.random_change(g)
        c = solution_generator.calculate_cost(g)
        if best_child_cost is None:
            best_child_cost = c
            children = g
        if c < best_child_cost:
            best_child_cost = c
            children = g
        if c < min_cost:
            min_cost = c
            best_grid = g
            absolute_best_grid = g
            take_first = False
            epoch_count = 0
            generation += 1
    if epoch_count % 10 == 0:
        print('Generation', generation, 'Age:', epoch_count, 'Min cost:', min_cost)
    if take_first is True:
        print('Taking first.')
        min_cost = best_child_cost
        best_grid = children
        take_first = False
        epoch_count = 0
    epoch_min_cost = min_cost
    if min_cost == 0:
        break
    epoch_count += 1
    if epoch_count > 1000 and epoch_min_cost == min_cost:
        print('No changes. Best child will be next parent.')
        take_first = True
        epoch_count = 0
        generation += 1

print('Final cost:', min_cost)
print('H:', solution_generator.cost_horizontal(absolute_best_grid))
print('V:', solution_generator.cost_vertical(absolute_best_grid))
print('C:', solution_generator.cost_cells(absolute_best_grid))
print(absolute_best_grid)

currentDT = datetime.datetime.now()
print('Start: ', str(startTime))
print('Finish:', str(currentDT))

