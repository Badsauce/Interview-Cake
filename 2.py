def get_products_of_all_ints_except_at_index(input_list):
    list_length = len(input_list)

    output_list = [1 for x in range(list_length)]

    total_product = 1

    for index in range(list_length-1):
        total_product *= input_list[index]
        output_list[index+1] *= total_product

    total_product = 1

    for index in range(list_length-1,0,-1):
        total_product *= input_list[index]
        output_list[index-1] *= total_product
        

    return output_list

print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
