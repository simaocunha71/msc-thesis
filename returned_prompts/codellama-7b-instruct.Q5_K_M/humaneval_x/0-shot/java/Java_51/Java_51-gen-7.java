        String[] words = text.split(" ");
        String longestWord = words[0];
        for (String word : words) {
            if (word.length() > longestWord.length()) {
                longestWord = word;
            }
        }
        return longestWord;
    }

    /**
    longestWord is a function that takes a string and returns the longest word in it.
    >>> longestWord("")
    ""
    >>> longestWord("aa bb cc")