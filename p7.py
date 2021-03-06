from math import ceil, log

# upper bound of prime number is n[ln(n) + ln(ln(n)) ]
def upper_bound(n):
    return ceil(n * (log(n) + log(log(n))))

# ub => upperbound
def get_primes(ub):
    nums = [True] * (ub + 1)
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i*i, ub + 1, i):
                nums[n] = False

def get_nth_prime(n):
    primes = list(get_primes(upper_bound(n)))
    return primes[n - 1]

print(get_nth_prime(10001))