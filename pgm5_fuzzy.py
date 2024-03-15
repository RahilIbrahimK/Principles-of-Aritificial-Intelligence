# union and intersection of two fuzzy sets
def fuzzy_union(set1, set2):
    union_set = {}
    for element in set1:
        union_set[element] = max(set1[element], set2.get(element, 0))
    for element in set2:
        if element not in union_set:
            union_set[element] = set2[element]
    return union_set

def fuzzy_intersection(set1, set2):
    intersection_set = {}
    for element in set1:
        if element in set2:
            intersection_set[element] = min(set1[element], set2[element])
    return intersection_set

def display_fuzzy_set(fuzzy_set):
    print("{", end="")
    for element, membership in fuzzy_set.items():
        print(f"{element}: {membership}", end=" ")
    print("}")

# Example fuzzy sets
set1 = {'a': 0.8, 'b': 0.6, 'c': 0.4, 'd': 0.2, 'e': 0.1}
set2 = {'a': 0.7, 'b': 0.5, 'c': 0.3, 'f': 0.9, 'g': 0.4}

print("Fuzzy set 1:")
display_fuzzy_set(set1)

print("\nFuzzy set 2:")
display_fuzzy_set(set2)

print("\nUnion of the fuzzy sets:")
union_set = fuzzy_union(set1, set2)
display_fuzzy_set(union_set)

print("\nIntersection of the fuzzy sets:")
intersection_set = fuzzy_intersection(set1, set2)
display_fuzzy_set(intersection_set)

# set1 = {'a': 0.8, 'b': 0.6, 'c': 0.4, 'd': 0.2, 'e': 0.1}
# set2 = {'a': 0.7, 'b': 0.5, 'c': 0.3, 'f': 0.9, 'g': 0.4}

# # Union of set1 and set2
# x = {key: max(set1.get(key, 0), set2.get(key, 0)) for key in set1.keys() | set2.keys()}
# print(f"Union is {x}")

# # Intersection of set1 and set2
# y = {key: min(set1.get(key, 0), set2.get(key, 0)) for key in set1.keys() & set2.keys()}
# print(f"Intersection is {y}")
# union = {**set1, **set2}
# print(f"Union is {union}")