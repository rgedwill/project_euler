# # Number Splitting
from math import pow

def check_digit_sum(num, total):
    digit_list = [int(x) for x in str(int(num))]
    L, R = 0, 0
    
    for i in digit_list:
        print(i)


def main():
    # for i in range(1, 10_000_001):
    for root in range(1, 10_000):
        sq = pow(root, 2)
        digit_sum = sum([int(root) for root in str(int(sq))])
        if sq == 6724:
            print(int(sq), digit_sum)
        if digit_sum == sq:
            print(sq)

check_digit_sum(6724, 72)