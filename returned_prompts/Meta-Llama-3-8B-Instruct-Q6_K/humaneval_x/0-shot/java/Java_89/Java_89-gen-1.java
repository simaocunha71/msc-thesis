```java
public String encrypt(String s) {
    StringBuilder result = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (Character.isLetter(c)) {
            char base = Character.isUpperCase(c) ? 'A' : 'a';
            result.append((char) ((c - base + 8) % 26 + base));
        } else {
            result.append(c);
        }
    }
    return result.toString();
}
```


Here is the explanation of the code:

1.  We create a `StringBuilder` called `result` to store the encrypted string.
2.  We iterate over each character `c` in the input string `s` using a for-each loop.
3.  We check if the character `c` is a letter using `Character.isLetter(c)`. If it is not a letter, we simply append it to the `result` as is.
4.  If the character `c` is a letter, we determine whether it is uppercase or lowercase using `Character.isUpperCase(c)`. We then calculate the new character by shifting the original character down by 8 places (2 \* 2) using the modulo operator (`% 26`). We add the base character ('A' for uppercase or 'a' for lowercase) to get the final encrypted character.
5.  We append the encrypted character to the `result` using `result.append((char) ((c - base + 8) % 26 + base));`.
6.  Finally, we return the encrypted string as a `String` by calling `result.toString()`.

This code effectively rotates the alphabet by 8 places, as required in the problem statement. It handles both uppercase and lowercase letters correctly and leaves non-letter characters unchanged.