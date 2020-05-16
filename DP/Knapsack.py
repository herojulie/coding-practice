# item can get used once


items = [{'value': 15, 'weight': 15},
         {'value': 10, 'weight': 12},
         {'value': 8, 'weight': 10},
         {'value': 1, 'weight': 5}]
capacity = 22

# in case, no item is selected
cols = len(items) + 1
rows = capacity + 1
knapsack = [0] * rows
for i in range(rows):
    knapsack[i] = [0] * cols

for i in range(rows):
    knapsack[i][0] = 0
for i in range(cols):
    knapsack[0][i] = 0

for i in range(1, cols):
    for b in range(1, rows):
        weight = items[i-1]['weight']
        value = items[i-1]['value']
        if weight <= b:
            knapsack[b][i] = max(knapsack[b][i-1], value + knapsack[b-weight][i-1])
        else:
            knapsack[b][i] = knapsack[b][i-1]

for i in range(rows):
    print(knapsack[i])

print('answer:', knapsack[rows-1][cols-1])










