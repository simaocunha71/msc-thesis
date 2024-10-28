        List<String> words = new ArrayList<String>();
        String[] temp = s.split("[ ,]+");
        for(String str : temp){
            words.add(str);
        }
        return words;
    }
}

In this solution, the method wordsStrings accepts a string s. It first splits the string s into an array of words based on commas or spaces using the split method of the string class. Then it loops over each word in the array and adds it to a list. Finally it returns the list of words.

The regular expression "[ ,]+" used in the split method is a pattern that matches one or more occurrences of either a comma or a space. The plus sign (+) means one or more of the preceding element.

The split method returns an array of strings, so we convert it into a list for easier manipulation.

The time complexity of this solution is O(n), where n is the length of the string. This is because we need to go through each character in the string once to split it into words. The space complexity is also O(n), as we are storing the words in a list.

The method returns a list of words, so it can be used in any context where you need to work with a list of words from a string.

Note: This solution assumes that words are defined as one or more non-space characters separated by spaces or commas. If you have a different definition of a word, you will need to adjust the regular expression accordingly.
