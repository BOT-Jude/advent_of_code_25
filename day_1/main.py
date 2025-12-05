

import math


def count_zeros(prev, next):

    tally = 0

    # axiom 1: there are no moves with 0 width
    if prev == next: raise Exception("False!")

    # # lemma 1: x -> z and z -> x result in the same number of 0 crosses
    # if prev > next: prev, next = next, prev # s.t. prev is always less than next
    # lemma 1 is actually false because 50 -> 0 crosses once but 0 -> 50 crosses zero times

    # by offsetting by 0.5 in the direction of travel we no longer have to care about the edge case
    # of landing on 0 (if we had landed on 0 we would definetly pass it after the transformation)
    # because this edge case does not exists, lemma 1 holds and we can solve the exercise

    # lemma 4: offsetting by 0.5 in the direction of movement and the counting times crossing 0
    # is equivelent to counting the times crossing 0 and the times landing on 0
    if next > prev:
        next += 0.5
        prev += 0.5
    else:
        next -= 0.5
        prev -= 0.5

    # lemma 1': x -> z and z -> x result in the same number of 0 crosses
    if prev > next: prev, next = next, prev # s.t. next is always greater than prev

    # lemma 2: x1 -> x3 = x1 -> x2 -> x3 where all transitions are in the same direction
    loops = (next - prev) // 100
    remainder = (next - prev) % 100
    if remainder == 0: # we cannot have any empty moves
        remainder = 100
        loops -= 1

    # lemma 3: transitions of 100 always cross 0 exactly once
    tally += loops
    
    # align s.t. next is positive and less than 100
    final_move_end = next % 100
    final_move_start = (next % 100) - remainder

    if math.copysign(1, final_move_start) != math.copysign(1, final_move_end):
        tally += 1

    return tally


with open('input.txt') as f:
    count = 0
    pos = 50
    while line := f.readline().strip('\n'):
        prev_pos = pos
        if line[0] == 'R':
            pos += int(line[1:])
        elif line[0] == 'L':
            pos -= int(line[1:])
        else:
            raise Exception('Ahhh!')
        
        count += count_zeros(prev_pos, pos)


print(count)
