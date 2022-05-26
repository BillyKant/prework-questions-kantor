def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if max_num < num:
            max_num = num
    return max_num

num_list = [12, 54, 2, 7]
print(max_num_in_list(num_list))
