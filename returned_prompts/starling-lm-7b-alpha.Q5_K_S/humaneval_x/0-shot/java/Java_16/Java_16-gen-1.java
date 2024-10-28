    Set<Character> charSet = new HashSet<>();
    for (int i = 0; i < string.length(); i++) {
        char c = string.charAt(i);
        c = Character.toLowerCase(c);
        charSet.add(c);
    }
    return charSet.size();
    }
}




```

This program takes in a string as an argument and finds out how many distinct characters it consists of, regardless of case. It does so by converting all characters to lowercase and adding them to a set. Since a set does not allow duplicate entries, the size of the set after adding all characters will be the number of distinct characters in the string.

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the string once to add each character to the set. The space complexity is also O(n), as the size of the set can be at most equal to the length of the input string.

The solution is implemented in the `countDistinctCharacters` method of the `Solution` class. It takes a string as an argument and returns an integer representing the number of distinct characters in the string.

Here are some example test cases for the `countDistinctCharacters` method:

```
>>> countDistinctCharacters("xyzXYZ")
3
>>> countDistinctCharacters("Jerry")
4
```

In the first test case, the string "xyzXYZ" consists of three distinct characters: 'x', 'y', and 'z'. In the second test case, the string "Jerry" consists of four distinct characters: 'j', 'e', 'r', and 'y'. The solution correctly counts the number of distinct characters in each string.

Overall, this solution provides an efficient and accurate way to determine the number of distinct characters in a given string.

```

```