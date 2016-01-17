def find_ending_paren(string,index_of_beginning_paren):
    if string[index_of_beginning_paren] == '(':
        unpaired_parens = 1
        for index in range(index_of_beginning_paren+1,len(string)):

            if string[index] == ')':
                unpaired_parens -= 1

            if string[index] == '(':
                unpaired_parens += 1

            if unpaired_parens == 0:
                return index

        print('Error: End of String reached without finding a ending paren')
        return -1
    else:
        print('Error: The beginning index supplied does not point to a "("')
        return -1

test_string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(find_ending_paren(test_string,10))
