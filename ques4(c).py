sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89,11,89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Printing count of each item  ", count_dict)