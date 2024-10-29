from typing import Optional

import data
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(T1: data.Time,T2: data.Time ):
    total_sec = T1.second + T2.second
    remaining_seconds = total_sec%60
    remaining_min = total_sec - remaining_seconds
    add_min = remaining_min//60
    total_min = T1.minute + T2.minute + add_min
    total_hour = T1.hour +T2.hour

    return data.Time(total_hour,total_min,remaining_seconds)


# Part 4
def is_descending(lst:list[float])->bool:
    if len(lst) < 2:
        return True
    for i in range(1,len(lst)):
        if lst[i]>= lst[i-1]:
            return False
    return True




# Part 5
def largest_between(lst: list[int], lower: int, upper: int) -> Optional[int]:
    max_index = lower
    if lower>upper:
        return None

    for i in range(lower, upper + 1):
        if lst[i] > lst[max_index]:
            max_index = i

    return max_index



# Part 6
def furthest_from_origin(points: list[data.Point]) -> Optional[int]:
    if len(points) == 0:
        return None

    max_index = 0
    max_distance = math.sqrt(points[0].x ** 2 + points[0].y ** 2)

    for i in range(1, len(points)):
        distance = math.sqrt(points[i].x ** 2 + points[i].y ** 2)


        if distance > max_distance:
            max_index = i
            max_distance = distance
    return max_index

