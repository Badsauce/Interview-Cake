def reverse_interval(input_list,start,end):
    left_pointer = start
    right_pointer = end-1
    while left_pointer < right_pointer:
        temp = input_list[left_pointer]
        input_list[left_pointer] = input_list[right_pointer]
        input_list[right_pointer] = temp
        
        left_pointer += 1
        right_pointer -= 1

def reverse_words(words):
    #cast to a mutable list
    word_list = list(words)
    reverse_interval(word_list,0,len(word_list))

    word_begin = 0
    word_end = -1

    for char in word_list:
        word_end += 1
        if char == ' ':
            reverse_interval(word_list,word_begin,word_end)
            word_begin = word_end+1

    reverse_interval(word_list,word_begin,word_end+1)

    return ''.join(word_list)

print(reverse_words('find you will pain only go you recordings security the into if'))
print(reverse_words(''))
print(reverse_words(' find you will pain only go you recordings security the into if '))
