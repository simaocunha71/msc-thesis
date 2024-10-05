Here is a Java solution for the problem:

```java
public String encode(String message) {
    StringBuilder encodedMessage = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isUpperCase(c)) {
            encodedMessage.append(Character.toLowerCase(c));
        } else {
            encodedMessage.append(Character.toUpperCase(c));
        }

        if ("aeiou".contains(Character.toString(c))) {
            encodedMessage.append((char) (c + 2));
        }
    }
    return encodedMessage.toString();
}
```

This function uses a `StringBuilder` to construct the encoded message. It iterates over each character in the input message. If the character is uppercase, it appends its lowercase equivalent to the `StringBuilder`. If the character is lowercase, it appends its uppercase equivalent. If the character is a vowel (a, e, i, o, u), it appends the character that appears 2 places ahead of that vowel in the English alphabet. Finally, it returns the encoded message as a string.

Note: This solution assumes that the input message contains only letters. If the input message can contain other characters (such as numbers or punctuation), the function should be modified to handle those characters appropriately.