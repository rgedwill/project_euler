# Summation of primes
from math import ceil, log

def get_primes(ub):
    nums = [True] * (ub + 1)
    nums[0] = nums[1] = False
    for(i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i*i, ub+1, i):
                nums[n] = False

def sum_primes(ub):
    l = list(get_primes(ub))
    return sum(l)

print(sum_primes(2000000))
    
