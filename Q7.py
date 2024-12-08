def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
result = has_duplicates(example_list)
print(f"Has duplicates: {result}")
