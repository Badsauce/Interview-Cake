def find_duplicate(list_of_numbers):
    n = len(list_of_numbers)-1
    no_duplicate_sum = (n+1)*n/2

    duplicate_sum = 0
    for number in list_of_numbers:
        duplicate_sum += number


    return duplicate_sum - no_duplicate_sum

print(find_duplicate([1,2,3,4,5,5]))
