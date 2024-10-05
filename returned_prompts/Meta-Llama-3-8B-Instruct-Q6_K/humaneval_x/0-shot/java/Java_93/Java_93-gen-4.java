```java
public String encode(String message) {
    StringBuilder sb = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            char base = Character.isUpperCase(c) ? 'A' : 'a';
            if (base == 'a' || base == 'e' || base == 'i' || base == 'o' || base == 'u') {
                sb.append((char) ((base + 2 - 'a') % 26 + 'a'));
            } else {
                sb.append((char) ((base + 2 - 'A') % 26 + 'A'));
            }
        } else {
            sb.append(c);
        }
    }
    return sb.toString();
}
```
This solution iterates over each character in the message. If the character is a letter, it checks if it's a vowel (a, e, i, o, u). If it is, it replaces it with the letter that appears 2 places ahead in the alphabet. If it's not a vowel, it simply changes the case of the letter. If the character is not a letter, it leaves it as is. The result is appended to a StringBuilder, which is then converted to a string and returned. The % operator is used to ensure that the result wraps around the alphabet if necessary. For example, if the letter is 'z' and we want to move 2 places ahead, we would get 'b'. The % 26 operation ensures that this wrapping around the alphabet happens correctly.