    int maxUnique = Integer.MIN_VALUE;
    String maxWord = "";

    for (String word : words) {
        int unique = (int) word.chars().distinct().count();
        if (unique > maxUnique) {
            maxUnique = unique;
            maxWord = word;
        } else if (unique == maxUnique) {
            if (word.compareTo(maxWord) < 0) {
                maxWord = word;
            }
        }
    }

    return maxWord;
}
}

This program uses Java Streams to count the distinct characters in each string. It then compares this count to the maximum count found so far, updating the max if necessary. In the event of a tie, it uses the Java String compareTo method to break the tie by choosing the string that comes first in lexicographical order. The function finally returns the string with the most unique characters.

Note: The function will return an empty string if all words are made up of repeating characters.


This problem also can be solved with the help of Hashset in Java.



