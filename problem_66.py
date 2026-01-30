# Problem 66: Find intersection of two lists
# Find and fix the error

def intersection(list1, list2):
    result = []
    seen = set()
    list2_set = set(list2)
    for item in list1:
        if item in list2_set and item not in seen:
            result.append(item)
            seen.add(item)
    return result

l1 = [1, 2, 2, 3, 4]
l2 = [2, 3, 4, 4, 5]
print(f"Intersection: {intersection(l1, l2)}")
