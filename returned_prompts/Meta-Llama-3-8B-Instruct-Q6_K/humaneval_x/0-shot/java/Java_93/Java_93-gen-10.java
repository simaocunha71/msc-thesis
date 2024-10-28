```java
public String encode(String message) {
    StringBuilder result = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            char base = Character.isUpperCase(c) ? 'A' : 'a';
            char newChar = (char) ((c - base + 2) % 26 + base);
            result.append(newChar);
        } else {
            result.append(c);
        }
    }
    return result.toString();
}
```
Explanation:
The function iterates over each character in the input message. If the character is a letter, it checks whether it's uppercase or lowercase. If it's uppercase, it subtracts the ASCII value of 'A' from the character, adds 2, and takes the modulus 26 to get the new character. If the character is lowercase, it does the same but with the ASCII value of 'a'. The result is appended to a StringBuilder. If the character is not a letter, it's simply appended to the StringBuilder as is. Finally, the function returns the resulting string.