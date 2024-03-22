"""

Reverse a string

str = hope

result = epoh
"""

def reverse_string():
    print("reversing string")


def two_sum(num, target):
    for i,val in enumerate(num):
       search_value = target - val
       if search_value in num:
           return [i, num.index(search_value)]
    return []

print(two_sum(num=[2,11,15,7], target=9))
