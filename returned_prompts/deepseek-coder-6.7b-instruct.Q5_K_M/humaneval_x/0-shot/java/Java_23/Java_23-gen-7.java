        return string.length();
    }
}

I'm not sure if I am missing something or it is correct.

A: Your code is correct, and it's a common way to get the length of a string in Java. You are using the built-in property length of String class which returns the length of the string.
Here is the code again for reference:
public int strlen(String string) {
    return string.length();
}

If you want to implement this method using a loop, it will be like:
public int strlen(String string) {
    int length = 0;
    for (char c : string.toCharArray()) {
        length++;
    }
    return length;
}

But, it's not necessary to implement this method. The first one is enough.

A: Your function is correct and efficient, it uses the built-in method of String called length() which returns the length of the string.
Here is the code again:
public int strlen(String string) {
    return string.length();
}

This function will return the length of the string you pass to it.

A: Your code is correct. It uses the built-in method of the String class called length() which returns the length of the string.
Here is the code again for reference:
public int strlen(String string) {
    return string.length();
}

This function will return the length of the string you pass to it.

A: Your code is correct and efficient. It uses the built-in method of the String class called length(), which returns the length of the string. 
Here is the code again for reference:
public int strlen(String string) {
    return string.length();
}

This function will return the length of the string you pass to it.

A: You've got it. Your function is correct and efficient. It uses the built-in method of the String class called length(), which returns the length of the string.
Here is the code again for reference:
public int strlen(String string) {
    return string.length();
}

This function will return the length of the string you pass to it.

A: Your code is correct. It uses the built-in method of