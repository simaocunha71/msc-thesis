```java
public String encode(String message) {
    StringBuilder result = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            char base = Character.toLowerCase(c);
            if (base == 'a' || base == 'e' || base == 'i' || base == 'o' || base == 'u') {
                base += 2;
                if (base > 'z') {
                    base -= 26;
                }
            } else {
                base = Character.toUpperCase(base);
            }
            result.append(base);
        } else {
            result.append(c);
        }
    }
    return result.toString();
}
```
The provided solution iterates through each character in the input message. If the character is a letter, it checks if it's a vowel. If it is, it increments the character by 2 (wrapping around to the beginning of the alphabet if necessary). If it's not a vowel, it converts it to uppercase. Finally, it appends the resulting character to the result string. If the character is not a letter, it simply appends it to the result string unchanged. The resulting string is then returned.