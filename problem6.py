sum_of_squares = sum(x**2 for x in range(101))
square_of_sum = sum(range(101)) ** 2

result = square_of_sum - sum_of_squares
print(result)
