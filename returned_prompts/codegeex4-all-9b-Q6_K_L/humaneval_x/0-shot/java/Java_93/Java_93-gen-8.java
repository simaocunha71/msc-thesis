Here is a simple solution in Java. It loops over each character in the string, checks if it is a vowel and if so replaces it with the next vowel in the alphabet. It also changes the case of each character to the opposite.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(encode("test"));
        System.out.println(encode("This is a message"));
    }
    public static String encode(String message) {
        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (isVowel(c)) {
                c = getNextVowel(c);
            }
            encodedMessage.append(c == Character.toUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
        }
        return encodedMessage.toString();
    }

    private static boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }

    private static char getNextVowel(char c) {
        String vowels = "AEIOUaeiou";
        int index = vowels.indexOf(c);
        return vowels.charAt((index + 2) % vowels.length());
    }
}
```

In this solution, `isVowel` checks if a character is a vowel by seeing if it is in the string "AEIOUaeiou". `getNextVowel` gets the next vowel in the alphabet by finding the current vowel in the string "AEIOUaeiou", adding 2 to the index, and taking the character at that index in the string. The modulo operator (%) is used to wrap around to the beginning of the string if the index goes past the end.

The `encode` function iterates over each character in the input string, checks if it is a vowel and if so replaces it with the next vowel in the alphabet. It also changes the case of each character to the opposite. The encoded characters are appended to a `StringBuilder`, which is then converted to a string and returned.