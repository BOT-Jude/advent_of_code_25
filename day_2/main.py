
import math


print("Hello world, and good luck!")

def diff(lower_pal, upper_pal):

    if upper_pal < lower_pal:
        return 0
    
    if upper_pal == lower_pal:
        return lower_pal

    first_lower = lower_pal[:len(lower_pal)//2]
    first_upper = upper_pal[:len(upper_pal)//2]

    # the sum of the intermediate pals
    # is the sum of all there lower digits (which has a nice closed form solution)
    lower_total = ((upper_pal * (upper_pal + 1)) // 2) - ((lower_pal * (lower_pal + 1)) // 2) 

    # plus the sum of their higher digits with the associated left shifts
    # which is much harder
    # you can group the sums by the left shift required but it's kinda gross

    ndigits_lower = len(lower_pal)
    ndigits_upper = len(upper_pal)

    for i in range(ndigits_lower//2, (ndigits_upper//2) + 1):
        pass




def get_minimal_pal(n):
    ndigits = len(n)
    if ndigits % 2 == 1:
        first = math.pow(10, (ndigits // 2) + 1)
        return str(first) + str(first)
    else:
        first_n = int(n[:ndigits//2])
        last_n = int(n[ndigits//2:])
        if last_n > first_n:
            return str(first_n + 1) + str(first_n + 1)
        else:
            return str(first_n) + str(first_n)

def get_maximal_pal(n):
    ndigits = len(n)
    if ndigits % 2 == 1:
        first = math.pow(10, (ndigits // 2) + 1) - 1
        return str(first) + str(first)
    else:
        first_n = int(n[:ndigits//2])
        last_n = int(n[ndigits//2:])
        if last_n > first_n:
            return str(first_n) + str(first_n)
        else:
            return str(first_n-1) + str(first_n-1)

def sum_contained_pals(start, end):

    # lemma 1: given pal d1->dn : d1->dn then next highest pal is (d1->dn) + 1 : (d1->dn) + 1

    # lemma 2: given a number with an even number of digits (d1->dn : dn->d2n),
    #  d1->dn-1 : d1->dn-1 is definetly less than it
    #  d1->dn+1 : d1->dn+1 is definetly greater than it

    # lemma 3: given a number with an odd number of digits
    # the minimal is 9...9 with one fewer digits
    # the maximal is 10..10.. with one greater digits

    min_maximal = get_maximal_pal(start)
    max_minimal = get_minimal_pal(end)

    return diff(min_maximal, max_minimal)

if __name__ == '__main__':

    with open('input.txt') as f:
        ranges = [block.split('-') for block in f.readline().strip('\n').split(',')]
        print(sum([sum_contained_pals(start, end) for start, end in ranges]))