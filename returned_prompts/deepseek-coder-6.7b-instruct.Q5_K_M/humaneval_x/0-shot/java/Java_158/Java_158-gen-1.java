It seems that you have a wrong answer. The correct answer should be "aaaaaaa". The word "aaaaaaa" has the maximum number of unique characters (1) and comes first in lexicographical order among the given words. 

So, the corrected code should be:

```java
public String findMax(List<String> words)  {

    String maxWord = "";
    int maxUnique = 0;

    for (String word : words) {
        Set<Character> uniqueChars = new HashSet<>();
        for (char c : word.toCharArray()) {
            uniqueChars.add(c);
        }

        if (uniqueChars.size() > maxUnique) {
            maxUnique = uniqueChars.size();
            maxWord = word;
        } else if (uniqueChars.size() == maxUnique) {
            maxWord = maxWord.compareTo(word) < 0 ? maxWord : word;
        }
    }

    return maxWord;
}
```

This code works by iterating over each word in the list, then adding each character to a HashSet. The size of the HashSet gives us the number of unique characters in the word. If this number is greater than the current maximum unique characters found, we update the maximum and the word. If it is equal, we compare the words lexicographically and update if the current word comes before the current maximum word. Finally, we return the word with the maximum unique characters.

So, for the