        List<String> wordList = new ArrayList<>();
        String[] words = s.split("[\\s,]+");
        for(String word : words) {
            wordList.add(word);
        }
        return wordList;
    }
}

This solution uses Java's built-in string method split() to split the string into words. The regular expression "[\\s,]+" is used to split the string by either one or more spaces or commas. The split() method returns an array of strings, which is then converted into a list and returned. 

The time complexity of this solution is O(n), where n is the length of the string. This is because the split() method and the for loop iterate through the string once. The space complexity is also O(n), as a new list is created to store the split words.

The code assumes that the input string is not null and is not empty. If this is not the case, additional error checking should be added.
