Here is a solution using Java:

```java
public String encode(String message) {
    StringBuilder encodedMessage = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            if (Character.isLowerCase(c)) {
                c = Character.toUpperCase(c);
            } else {
                c = Character.toLowerCase(c);
            }
            if ("AEIOUaeiou".contains(String.valueOf(c))) {
                if (c == 'a' || c == 'A') {
                    c = 'c';
                } else if (c == 'e' || c == 'E') {
                    c = 'g';
                } else if (c == 'i' || c == 'I') {
                    c = 'k';
                } else if (c == 'o' || c == 'O') {
                    c = 'q';
                } else if (c == 'u' || c == 'U') {
                    c = 'w';
                }
            }
        }
        encodedMessage.append(c);
    }
    return encodedMessage.toString();
}
```

This function iterates through each character of the input message. If the character is a letter, it swaps its case. If the character is a vowel, it replaces it with the corresponding letter 2 places ahead in the alphabet. Finally, it appends the character to a StringBuilder object, which is then converted to a String and returned.