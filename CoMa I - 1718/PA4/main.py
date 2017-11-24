"""
Calculates an intervall which will include the golden ratio (1 + sqrt(5))/2 to
a certain accurancy using fibonacci numbers. For a given number l the intervall
in which the golden ratio is approximated is defined as
I_l = [f_2l/f_2l-1, f_2l+1/f_2l] where f_n is the nth fibonacci number.

Args:
    accurancy: The desired accurancy 1/accurancy for the golden ratio. Just
    provide the denominator of the accurancy.

Returns:
    A list of three elements. The first element represents the number l used
    for defining the intervall. The second element is a tuple which represents
    the lower bound of the intervall (the first element is the numerator and the
    second element is the denominator). The third element is a tuple which
    represents the upper bound of the intervall (the first element is the
    numerator and the second element is the denominator).
"""
def intervall_for_golden_ratio(accurancy):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    l = 2
    while True:
        while (len(fibonacci) <= 2 * l + 1):
            n = len(fibonacci)
            fibonacci.append(fibonacci[n - 2] + fibonacci[n - 1])
        a = fibonacci[2 * l + 1]
        b = fibonacci[2 * l]
        c = fibonacci[2 * l - 1]
        d = fibonacci[2 * l - 2]
        e = fibonacci[2 * l - 3]
        if (accurancy * (-1)**(2*l) < b * c):
            if (d * e <= accurancy * (-1)**(2*l - 2)):
                answer = []
                answer.append(l)
                answer.append((b, c))
                answer.append((a, b))
                return answer
        l += 1


# print(intervall_for_golden_ratio(1))
# print(intervall_for_golden_ratio(6))
# print(intervall_for_golden_ratio(100))
# print(intervall_for_golden_ratio(10**855))
