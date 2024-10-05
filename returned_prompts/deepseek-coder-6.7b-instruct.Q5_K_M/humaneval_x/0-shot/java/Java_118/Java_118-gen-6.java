    char[] vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    List<Character> vowelList = Arrays.asList(vowels);
    int lastVowelIndex = -1;
    for (int i = word.length() - 1; i > 0; i--) {
        if (vowelList.contains(word.charAt(i))) {
            lastVowelIndex = i;
            break;
        }
    }

    if (lastVowelIndex == -1) {
        return "";
    }

    int minDistance = Integer.MAX_VALUE;
    char closestVowel = ' ';
    for (int i = lastVowelIndex - 1; i > 0; i--) {
        if (!vowelList.contains(word.charAt(i))) {
            if (lastVowelIndex - i < minDistance) {
                minDistance = lastVowelIndex - i;
                closestVowel = word.charAt(i);
            }
        }
    }

    return closestVowel == ' ' ? "" : String.valueOf(closestVowel);
}
}

The code above is a solution to the problem. This problem can be solved by first finding the last vowel in the word and then looking for the closest vowel that is on the left side of the last found vowel.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
