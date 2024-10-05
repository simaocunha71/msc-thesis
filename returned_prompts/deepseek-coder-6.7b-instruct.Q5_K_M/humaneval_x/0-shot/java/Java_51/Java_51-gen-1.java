        StringBuilder sb = new StringBuilder();
        String vowels = "aeiouAEIOU";

        for (char c: text.toCharArray()) {
            if (vowels.indexOf(c) == -1) {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}


A: If you want to remove only the lowercase vowels, then you can modify the code like this:

```java
public String removeVowels(String text) {
    StringBuilder sb = new StringBuilder();
    String vowels = "aeiou";

    for (char c: text.toCharArray()) {
        if (vowels.indexOf(c) == -1) {
            sb.append(c);
        }
    }

    return sb.toString();
}
```

This version of the function will not remove any uppercase vowels.

If you want to remove both uppercase and lowercase vowels, then you can simply add the uppercase vowels to the list of characters to remove:

```java
public String removeVowels(String text) {
    StringBuilder sb = new StringBuilder();
    String vowels = "aeiouAEIOU";

    for (char c: text.toCharArray()) {
        if (vowels.indexOf(c) == -1) {
            sb.append(c);
        }
    }

    return sb.toString();
}
```

This version of the function will remove both uppercase and lowercase vowels from the input string.

In both cases, the function works by iterating over each character in the input string. If the character is not a vowel (i.e., it is not in the "aeiouAEIOU" string), then it is appended to the output string. If the character is a vowel, it is skipped. The function returns the output string, which contains the same characters as the input string, but without any vowels.

Note: The `indexOf` method returns -1 if the character is not found in the string. In the context of the function, this means that the character is not a vowel.

Also note that