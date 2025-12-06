
import math


print("Hello world, and good luck!")

def _p_sum(ndigits, limit=None):
    """
        Sum all ndigit pallendromic numbers up to limit
    """

    half_digits = ndigits//2

    half_upper = min(int(limit[:(len(limit)//2)]), int('9' * half_digits))
    half_lower = int('1' + '0' * (half_digits-1))

    lower_total = ((half_upper * (half_upper + 1)) // 2) - ((half_lower * (half_lower + 1)) // 2) + half_lower
    upper_total = (((half_upper * (half_upper + 1)) // 2) - ((half_lower * (half_lower + 1)) // 2) + half_lower) * int(math.pow(10, half_digits))

    return lower_total + upper_total

def p_sum(limit: str):
    """
        Sum all pallendromic numbers up to limit
    """
    ndigits = len(limit)
    half_digits = ndigits // 2
    assert ndigits % 2 == 0, limit
    assert ndigits > 0
    half_limit = limit[:half_digits]

    total = 0
    for i in range(1, half_digits+1):
        total += _p_sum(2*i, limit=limit)

    return total

def get_minimal_pal(n):
    """
        Get the lowest pallendromic number greater than or equal to 'n'
    """
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

def sum_contained_pals(start, end):

    lower_minimal = get_minimal_pal(start)
    upper_minimal = get_minimal_pal(str(int(end) + 1)) # must be strictly greater than

    return p_sum(upper_minimal) - p_sum(lower_minimal) - int(upper_minimal) + int(lower_minimal)

if __name__ == '__main__':

    with open('input.txt') as f:
        ranges = [block.split('-') for block in f.readline().strip('\n').split(',')]
        print(sum([sum_contained_pals(start, end) for start, end in ranges]))
