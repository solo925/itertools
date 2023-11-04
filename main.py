import itertools

# itertools.count()
count = itertools.count(1, 3)
print("counting odd numbers")
for _ in range(5):
    print(next(count))

# itertools.cycle()
colors = ["red", "blue", "green"]
cycle_iterator = itertools.cycle(colors)
print("cycling through colors")
for _ in range(5):
    print(next(cycle_iterator))

# itertools.combinations()
letters = ['a', 'b', 'c', 'd', 'e']
combinations = list(itertools.combinations(letters, 2))
print("\n combination of two letters: ", combinations)

# itertools.permutations()
numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers))
print("printing permutations")
print(permutations)

# itertools.product()
dice = list(itertools.product(range(1, 7), repeat=2))
print("\n possible outcome of rolling two dices: ", dice)
