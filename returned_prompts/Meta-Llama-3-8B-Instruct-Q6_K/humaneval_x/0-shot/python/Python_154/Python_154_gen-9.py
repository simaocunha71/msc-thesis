```
def cycpattern_check(a, b):
    for i in range(len(b)):
        if b in a[i:] + a[:i]:
            return True
    return False
```


The above function checks if the second word or any of its rotations is a substring in the first word. It does this by iterating over the second word and checking if it is a substring of the first word. The substring check is done by concatenating the end part of the first word with its start part, and then checking if the second word is in this concatenated string. If it finds a match, it returns True, otherwise it returns False. 

For example, for the input ("abcd","abd"), the function will iterate over the second word "abd" and check if it is a substring of the first word "abcd". Since "abd" is not a substring of "abcd", the function will return False. 

For the input ("hello","ell"), the function will iterate over the second word "ell" and check if it is a substring of the first word "hello". Since "ell" is a substring of "hello", the function will return True. 

This approach has a time complexity of O(n*m) where n is the length of the first word and m is the length of the second word. This is because in the worst case, the function has to iterate over the entire second word for each character in the first word.  However, this approach is efficient enough for most practical purposes. 

Please note that this function is case sensitive and treats uppercase and lowercase letters as different characters. If you want to make it case insensitive, you can convert both the words to lowercase or uppercase before checking for the substring.  For example, you can replace the line `if b in a[i:] + a[:i]:` with `if b.lower() in a[i:] + a[:i].lower():`.  However, this will also make the function treat "A" and "a" as the same character, which might not be what you want.  You can adjust the function to suit your specific requirements. 