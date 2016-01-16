def reverse_string(string):
    if len(string) < 2:
        return string
    
    #convert to mutable list
    list_string = []
    for char in string:
        list_string.append(char)

    for index in range(0,int(len(string)/2)):
        temp = list_string[len(string)-1-index]
        list_string[len(string)-1-index] = list_string[index]
        list_string[index] = temp

    return ''.join(char for char in list_string)

print(reverse_string('home'))    

    
