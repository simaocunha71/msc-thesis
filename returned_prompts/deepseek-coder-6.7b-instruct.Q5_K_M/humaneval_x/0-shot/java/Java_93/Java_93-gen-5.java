        StringBuilder encodedMsg = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                if (Character.isLowerCase(c)) {
                    encodedMsg.append(Character.toUpperCase(c));
                } else {
                    encodedMsg.append(Character.toLowerCase(c));
                }
            } else {
                encodedMsg.append(c);
            }
        }
        return encodedMsg.toString();
    }
}

Here's the solution to the problem:

This solution is to iterate through the message and for each character, check if it's an alphabet. If it is, then it is case swapped (if it's lowercase, it's made uppercase and vice-versa). If it's not an alphabet, it's left as it is.


A: You are using the built-in methods toLowerCase() and toUpperCase() which are not required for this problem. Instead you can directly compare the characters with their ASCII values to swap the case.
Here is the corrected code:
public String encode(String message)  {
    StringBuilder encodedMsg = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isAlphabetic(c)) {
            if (c >= 'a' && c <= 'z') {
                encodedMsg.append((char)(c - 'a' + 'A'));
            } else {
                encodedMsg.append((char)(c - 'A' + 'a'));
            }
        } else {
            encodedMsg.append(c);
        }
    }
    return encodedMsg.toString();
}

In this code, we are directly comparing the ASCII values of characters to check if they are uppercase or lowercase. And then swapping the case by adding or subtracting the difference between uppercase and lowercase ASCII values.

A: You can use the following code:
public String encode(String message) {
    StringBuilder encodedMsg = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isAlphabetic(c)) {