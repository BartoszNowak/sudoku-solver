import example
import solution_generator

example_grid = example.get_grid()

cost = solution_generator.calculate_cost(example_grid)
print(example_grid)
print('Initial cost:', cost)

min_cost = cost
best_grid = example_grid
take_first = False
epoch_count = 0
epoch_min_cost = min_cost
while True:
    for i in range(0, 10):
        g = best_grid.copy()
        g = solution_generator.random_change(g)
        g = solution_generator.random_change(g)
        g = solution_generator.random_change(g)
        c = solution_generator.calculate_cost(g)
        # print(g)
        print('Cost:', c)
        if c < min_cost or take_first is True:
            if take_first is True:
                print('Taking first.')
            min_cost = c
            best_grid = g
            take_first = False
    print('Min cost:', min_cost)
    epoch_min_cost = min_cost
    if min_cost <= 6:
        print('Min cost:', min_cost, '--------------------------------------------------------------')
        print(best_grid)
    if min_cost <= 4:
        break
    epoch_count += 1
    if epoch_count > 100 and epoch_min_cost == min_cost:
        print('No changes. Firs child will be next parent.')
        take_first = True
        epoch_count = 0

print('Min cost:', min_cost)
print(best_grid)
