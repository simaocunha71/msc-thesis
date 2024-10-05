Here is a solution in Java:

```java
public String encrypt(String s) {
    String alphabet = "abcdefghijklmnopqrstuvwxyz";
    String encrypted = "";
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (Character.isLetter(c)) {
            int index = alphabet.indexOf(Character.toLowerCase(c));
            if (index != -1) {
                int encryptedIndex = (index + 8) % alphabet.length();
                char encryptedChar = alphabet.charAt(encryptedIndex);
                if (Character.isLowerCase(c)) {
                    encrypted += encryptedChar;
                } else {
                    encrypted += Character.toUpperCase(encryptedChar);
                }
            } else {
                encrypted += c;
            }
        } else {
            encrypted += c;
        }
    }
    return encrypted;
}
```

This solution works by first defining the alphabet string. It then iterates through each character in the input string. If the character is a letter, it finds the index of the letter in the alphabet string and calculates the encrypted index by adding 8 to the original index and taking the modulus of the alphabet length. It then adds the encrypted character to the encrypted string, taking care to preserve the case of the original character. If the character is not a letter, it simply adds the character to the encrypted string. Finally, it returns the encrypted string.