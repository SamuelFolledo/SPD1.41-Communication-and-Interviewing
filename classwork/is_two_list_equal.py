# given 2 arrays (strings), return a bool if it's the same or not
# case sensitive with no white spaces

list1 = ["kobe", "mj", "lebron", "shaq", "dude",]
list2 = ["kobe", "shaq", "mj", "lebron", "other dude"]

#solution 1
def two_list_is_equal_a(list1, list2):
    cloned_list1 = list1
    for i in range(len(list2)):
        if list2[i] in cloned_list1:
            cloned_list1.remove(list2[i])
        else:
            return False
    if len(cloned_list1) != 0:
        return False
    return True

print("1A)",two_list_is_equal_a(list1, list2),"\n")

def two_list_is_equal_b(ar_1, ar_2):
    if len(ar_1) != len(ar_2):
        return False
    seen_items_set = set(ar_1)
    for item in ar_2:
        if item not in seen_items_set:
            return False
        seen_items_set.remove(item)
    if len(seen_items_set) > 0:
        return False
    return True

print("1B)",two_list_is_equal_b(list1, list2),"\n")