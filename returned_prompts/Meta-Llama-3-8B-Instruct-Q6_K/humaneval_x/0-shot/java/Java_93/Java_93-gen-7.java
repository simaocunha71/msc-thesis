```java
public String encode(String message) {
    StringBuilder result = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            char base = Character.isUpperCase(c) ? 'A' : 'a';
            if (base == 'a' || base == 'e' || base == 'i' || base == 'o' || base == 'u') {
                result.append((char) (base + 2));
            } else {
                result.append((char) (base + Character.isUpperCase(c) ? 1 : -1));
            }
        } else {
            result.append(c);
        }
    }
    return result.toString();
}
```

The solution works as follows:

1. It iterates over each character in the input string.
2. If the character is a letter, it checks if it is uppercase or lowercase.
3. If the letter is a vowel (a, e, i, o, u), it replaces it with the letter that appears 2 places ahead of it in the alphabet. For example, 'a' becomes 'c', 'e' becomes 'g', and so on.
4. If the letter is not a vowel, it swaps its case. For example, 'A' becomes 'a', 'a' becomes 'A', and so on.
5. If the character is not a letter (for example, a space or punctuation), it simply appends it to the result string without modification.
6. The final result string is returned.