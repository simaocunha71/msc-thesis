    StringBuilder sb = new StringBuilder();

B:
    char c = text.charAt(i);
    if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
        sb.append(c);
    }
    i++;
}
return sb.toString();


A: This is a simple task that can be achieved with StringBuilder in Java. 


*

*Create a new StringBuilder object.

*Iterate over each character in the string.

*Check if the character is not a vowel (either lowercase or uppercase).

*If it is not a vowel, append it to StringBuilder.

*Return the String representation of StringBuilder.


However, there's a small mistake in your code. You should increment the counter variable i in the loop, otherwise it will result in infinite loop as the condition i < text.length() is not changing.


