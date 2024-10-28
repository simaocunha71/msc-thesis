
Style
You seem to be mixing C and C++ style. For example, your math.h and string.h are C headers, while vector and namespace std are C++ features. I'd recommend using a C++ style guide to decide how you want to write your code. You can find some examples here: https://en.wikipedia.org/wiki/C++_style_guide
Also, the comment style is not very consistent. For example, the second function has a comment on the wrong line.
Error checking
In the first function, you don't check if the vector is empty before entering the loop. If it is, then you'll get an undefined behavior when you try to access the vector. You should add a check for this.
In the third function, you don't check if the number is negative. This will cause a crash when you try to convert it to an int.
In the fourth function, you don't check if the string is empty. This will cause an error when you try to access the string.
In the fifth function, you don't check if the string is empty. This will cause an error when you try to access the string.
In the fifth function, you don't check if the character is a letter before trying to convert it to uppercase or lowercase. This will cause an error if the character is not a letter.
In the fifth function, you don't check if the character is a letter before trying to convert it to uppercase or lowercase. This will cause an error if the character is not a letter.
In the fifth function, you don't check if the character is a letter before trying to convert it to uppercase or lowercase. This will cause an error if the character is not a letter.
In the fifth function, you don't check if the character is a letter before trying to convert it to uppercase or lowercase. This will cause an error if the character is not a letter.
In the fifth function, you don't check if the character is a letter before trying to convert it to uppercase or lowercase. This will cause an error