def merge_lists(list1, list2):
    merged_list = []
    list1_pointer = 0
    list2_pointer = 0

    while list1_pointer < len(list1) and list2_pointer < len(list2):
        if list1[list1_pointer] < list2[list2_pointer]:
            merged_list.append(list1[list1_pointer])
            list1_pointer += 1
        else:
            merged_list.append(list2[list2_pointer])
            list2_pointer += 1

    while list1_pointer < len(list1):
        merged_list.append(list1[list1_pointer])
        list1_pointer += 1

    while list2_pointer < len(list2):
        merged_list.append(list2[list2_pointer])
        list2_pointer += 1

    return merged_list

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_lists(my_list, alices_list))
