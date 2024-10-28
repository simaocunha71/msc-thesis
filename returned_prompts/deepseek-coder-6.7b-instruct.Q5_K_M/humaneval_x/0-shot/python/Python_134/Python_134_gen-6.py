
    def check_if_last_char_is_a_letter(txt):
        if txt and txt[-1].isalpha() and txt[-2] == ' ':
            return True
        else:
            return False

    print(check_if_last_char_is_a_letter("apple pie")) # False
    print(check_if_last_char_is_a_letter("apple pi e")) # True
    print(check_if_last_char_is_a_letter("apple pi e  ")) # False
    print(check_if_last_char_is_a_letter("")) # False

In this function, we first check if the string is not empty. Then, we check if the last character is an alphabetical character and if the character before it is a space (which means it's the end of a word).

This solution assumes that there will be no numbers in the string. If numbers are possible in the string, we would have to add an additional check to ensure that the character before the last character is also a space.

This solution also assumes that the string will only have spaces between words. If there may be other characters that are not spaces between words, we would have to add an additional check to ensure that the character before the last character is a space.

The time complexity of this solution is O(1), as it only performs a constant number of operations. The space complexity is also O(1), as it only uses a constant amount of memory.

'''
</pre>

'''
</code>
'''

</code>
</pre>
</details>

<details>
<summary>
<b>Solution 2: Using Regular Expressions</b>
</summary>
<code>
<pre>
'''
