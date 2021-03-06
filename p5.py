def greatest_common_denominator(a, b):
    while b:      
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return ((a * b) / greatest_common_denominator(a, b))

def least_common_multiple_range(li):
    if len(li) == 2:
        return least_common_multiple(li[0], li[1])
    else:
        check = li.pop()
        return least_common_multiple(check, least_common_multiple_range(li))

print(least_common_multiple_range([i for i in range(1, 21)]))