# Task 1
more = [x + 1 for x in [1, 2, 3, 4]] # List, in order, the values that x takes at each step. A: 1, 2, 3, 4
print() # What is the value of more at this point? A: more = [2, 3, 4, 5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. A: n = 1, return 1, n = 2, return 4, n = 3, return 9, n = 4, return 16
squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? A: [1, 4, 9, 16], same as values of n on previous calls

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. A: n = 0, return false, n = 1, return false, n = 2, return false, n = 3, return true, n = 4, return true

answer = [x for x in range(5) if check(x)]   # What is the value of answer? A: [3, 4]
print()

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value.
# m = 3, return 4, m = 4, return 5
def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
# A: n = 0, return false, n = 1, return false, n = 2, return false, n = 3, return true, n = 4, return true


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? A: [4, 5]
print()

# Task 2
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. A: total = 16, num = 1
    return total

result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    return new_list                    # How does this loop differ from that above? A: new_list = [4, 9, 2, 1], idx = 3, the first loop adds up the list while the second loop copies it to another list


result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. A: new_list = [5, 10, 3, 2], value = 1
    return new_list

result = increment_all([4, 9, 2, 1])

# Task 3

# Double the value of a number.
# Input: a number to be doubled
# Result: a number
def double(n:int) -> int:
    result = n * 2
    return result
