"""
Checks whether a given list of pairs of natural numbers is an equivalence
relation for {1, ..., n}.
Args:
    n: The biggest natural number (greater than 0) the equivalence relation
    should be based on.
    list: The list of relations (pairs of natural numbers).
Returns:
    True if the given list of pairs is an equivalence relation for {1, ..., n},
    False otherwise.
"""
def is_equivalence_relation(n, list):
    nodes = [set() for i in range(n + 1)]
    for pair in list:
        if pair[0] <= n:
            nodes[pair[0]].add(pair[1])
    for i in range(1, n + 1):
        if i not in nodes[i]:
            return False
        for edge in nodes[i]:
            if nodes[edge] != nodes[i]:
                return False
    return True


# print(is_equivalence_relation(1, [(1,1)]))
# print(is_equivalence_relation(1, [(2,2)]))
# print(is_equivalence_relation(4, [(1,1), (2,2), (3,3), (4,4)]))
# print(is_equivalence_relation(3, [(2,2), (1,1), (3,3), (4,4), (1,2), (2,1), (2,3), (3,2)]))
# print(is_equivalence_relation(2, [(1,1), (2,2), (1,2), (2,1), (1,1), (2,2)]))
