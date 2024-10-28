        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
            if (i == s.length() - 1 && c == 'y') {
                count++;
            }
        }
        return count;
    }
}

Explanation:
The code defines a function `vowelsCount` that takes a string `s` as input and returns the number of vowels in the string. The function iterates over each character `c` in the string using a for loop. It checks if the character is a vowel ('a', 'e', 'i', 'o', 'u') and increments the count if it is. It also checks if the character is 'y' and the index is the last index in the string (i.e., the character is at the end of the word) and increments the count if it is. Finally, the function returns the count of vowels. The time complexity is O(n), where n is the length of the input string. The space complexity is O(1), as it only uses a constant amount of space.