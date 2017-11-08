"""
Prints out the cross sums for a natural number for all positional notations
(https://en.wikipedia.org/wiki/Positional_notation) up to the given natural
number starting with base 2. For example, this means that
cross_sum_for_all_positional_notations(7) prints out 3, 3, 4, 3, 2, 1, because

base 2, cross sum of 111 is 3,
base 3, cross sum of 21 is 3,
base 4, cross sum of 13 is 4,
base 5, cross sum of 12 is 3,
base 6, cross sum of 11 is 2 and
base 7, cross sum of 10 is 1.

Args:
    number: The number for which the cross sums should be printed. It must be
    a natural number and bigger than 1.
"""
def cross_sum_for_all_positional_notations(number):
    if not isinstance(number, int) or number < 2:
        print("Please provide an integer > 1.")
        return
    i = 2
    result = ""
    while i <= number:
        result += str(cross_sum_for_base(number, i)) + ", "
        i += 1
    print(result[:-2])


def cross_sum_for_base(number, base):
    cross_sum = 0
    while (number > 0):
        cross_sum = number % base + cross_sum
        number = number // base
    return cross_sum
