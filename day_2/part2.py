
import math
import sympy


print("Hello world, and good luck!")

def get_maximal(d, i, limit):
    """
        Get the highest 'd' digit ('i')-palendromic number less than or equal to limit
    """
    assert len(limit) >= d
    assert d % i == 0

    k = d//i

    if len(limit) > d:
        return '9' * k
    else:



    ndigits = len(n)
    if ndigits % 2 == 1:
        first = int(math.pow(10, (ndigits // 2)))
        return str(first) + str(first)
    else:
        first_n = int(n[:ndigits//2])
        last_n = int(n[ndigits//2:])
        if last_n > first_n:
            return str(first_n + 1) + str(first_n + 1)
        else:
            return str(first_n) + str(first_n)

def _p_sum(d, i, limit):
    """
        Sum all 'd' digit ('i')-pallendromic numbers up to and (potentually) including limit
    """

    assert d % i == 0

    k = d//i

    upper = int(get_minimal(d, i, limit=limit)) # get the lowest 'd' digit ('i')-palendromic number greater than or equal to limit
    lower = 

    lower = int('1' + '0' * (k-1))
    cumulative_digit_sum = ((upper * (upper + 1)) // 2) - ((lower * (lower + 1)) // 2) + lower
    if upper > int(limit): cumulative_digit_sum -= upper
    total = cumulative_digit_sum * (sum([int(math.pow(10, k*j)) for j in range(i)]))
    if i != 1: total -= _p_sum(d, 1, limit=limit) # don't double count 1-pallendromic numbers

    return total

def p_sum(limit):

    total = 0
    for d in range(1, len(limit)+1):
        factors = sympy.primefactors(d)
        factors += [1]
        for i in factors:
            total += _p_sum(d, i, limit)

    return total

def sum_contained(start, end):

    return p_sum(start) - p_sum(str(int(end)-1))

if __name__ == '__main__':

    with open('input.txt') as f:
        ranges = [block.split('-') for block in f.readline().strip('\n').split(',')]
        print(sum([sum_contained(start, end) for start, end in ranges]))
