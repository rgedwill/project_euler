# even: n/2
# odd: 3n + 1
# largest chain starting with number < 1 million

def calculate_chains(n):
    num_chains = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        num_chains += 1
    return num_chains
    

def main():
    ans = 0
    ans_chains = 0

    for num in range(1, 1_000_000):
        num_chains = calculate_chains(num)
        if num_chains > ans_chains: 
            ans = num
            ans_chains = num_chains
    
    print(ans)

if __name__ == '__main__':
    main()