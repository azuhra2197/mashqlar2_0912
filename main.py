# 6
cubes = [x**3 for x in range(1, 6)]
print(cubes)

# 7
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)

# 8
animals = ["dog", "cat", "mouse"]
first_letters = [word[0] for word in animals]
print(first_letters)

# 9
numbers = [-5, 3, -1, 0, 7, -2]
positives = [x for x in numbers if x > 0]
print(positives)

# 10
even_odd = ["juft" if x % 2 == 0 else "toq" for x in range(1, 11)]
print(even_odd)
