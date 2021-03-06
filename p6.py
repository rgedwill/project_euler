# sum of squares formula:
# # [n(n + 1)(2n + 1)] / 6

def num_sum(n):
    return int(((1 + n) * n/2))

def square_of_sum(num):
    return num_sum(num) ** 2

def sum_of_squares(num):
    # return sum(i**2 for i in range(1, num+1))
    return ((num * (num + 1) * (2 * num + 1)) / 6)

def calc_ans(num):
    return square_of_sum(num) - sum_of_squares(num)

print(calc_ans(100))

