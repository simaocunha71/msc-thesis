It initializes a vector `count` of size 256 (since there are 256 ASCII characters) and initializes all elements of the vector as 0.

B:
It traverses the given string. For each character in the string, it increases the count of that character in the `count` array.

C:
It traverses the `count` array. If the count of a character is greater than 0, it means that character is present in the string. So, it increases the result `res` by 1.

D:
Finally, it returns the result `res` which is the number of distinct characters in the string.

## 6. Modify the program

You can modify the program to count the number of distinct characters in any string you want. To do this, replace the `str` variable in the main function with your own string.

## 7. What's next?

This program is a simple example of how to count the number of distinct characters in a string. You can take this concept