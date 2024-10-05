    def reverse_delete(s,c):
        # Create a list of all the characters in the string
        char_list = list(s)
        # Loop through the list and delete any characters that are in c
        for i in range(len(char_list)):
            if char_list[i] in c:
                del char_list[i]
        # Join the remaining characters and check if it is a palindrome
        new_string = ''.join(char_list)
        if new_string == new_string[::-1]:
            return (new_string, True)
        else:
            return (new_string, False)


