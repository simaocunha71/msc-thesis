    String closestVowel = "";
    String vowels = "aeiouAEIOU";
    String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

    for (int i = word.length()-2; i > 0; i--) {
        if (vowels.indexOf(word.charAt(i)) != -1 &&
            consonants.indexOf(word.charAt(i-1)) != -1 &&
            consonants.indexOf(word.charAt(i+1)) != -1) {
            closestVowel = String.valueOf(word.charAt(i));
            break;
        }
    }

    return closestVowel;
}
}


A: The problem is with the for loop condition. You are starting from the last character of the word and going to the first. You need to start from the second last character and go to the first.

Here is the corrected code:

```java
public String getClosestVowel(String word) {
    String closestVowel = "";
    String vowels = "aeiouAEIOU";
    String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

    for (int i = word.length()-2; i > 0; i--) {
        if (vowels.indexOf(word.charAt(i)) != -1 &&
            consonants.indexOf(word.charAt(i-1)) != -1 &&
            consonants.indexOf(word.charAt(i+1)) != -1) {
            closestVowel = String.valueOf(word.charAt(i));
            break;
        }
    }

    return closestVowel;
}
```

This code checks from the right side of the word for a vowel that is surrounded by consonants. If it finds one, it breaks the loop and returns that vowel. If it doesn't find any, it returns an empty string.

