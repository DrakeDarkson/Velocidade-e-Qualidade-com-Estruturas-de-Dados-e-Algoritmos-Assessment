def binary_search(isbns, target_isbn):
    left, right = 0, len(isbns) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if isbns[mid] == target_isbn:
            return mid, iterations
        elif isbns[mid] < target_isbn:
            left = mid + 1
        else:
            right = mid - 1

    return -1, iterations

def linear_search(isbns, target_isbn):
    iterations = 0

    for i, isbn in enumerate(isbns):
        iterations += 1
        if isbn == target_isbn:
            return i, iterations

    return -1, iterations

import random

# Gera uma lista ordenada de 100,000 ISBNs aleatórios
random.seed(42)
isbns = sorted(random.sample(range(1, 200000), 100000))

target_isbn = isbns[random.randint(0, 99999)]

binary_result, binary_iterations = binary_search(isbns, target_isbn)
linear_result, linear_iterations = linear_search(isbns, target_isbn)

print(f"Binary Search: Found at index {binary_result} in {binary_iterations} iterations.")
print(f"Linear Search: Found at index {linear_result} in {linear_iterations} iterations.")
