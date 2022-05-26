def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list))):
        return True
    else:
        return False 

list1 = [1, 2, 3, 4, 5]
list2 = [2, 5, 3, 1, 4]
print(is_consecutive(list1))
print(is_consecutive(list2))