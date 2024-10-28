        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            } else if (c == 'y' && i == s.length() - 1) {
                count++;
            }
        }
        return count;
    }
}

Solution:
The solution is a Java function named `vowelsCount` that takes a string `s` as input and returns the number of vowels in the string. The function iterates through each character in the string, and checks if the character is a vowel ('a', 'e', 'i', 'o', 'u') or 'y' at the end of the string. If the character is a vowel, it increments a counter. Finally, the function returns the counter.

The unit test `vowelsCount("abcde")` tests the function with a string that contains all the vowels, and the expected output is 2. The unit test `vowelsCount("ACEDY")` tests the function with a string that contains 'y' at the end, and the expected output is 3.

The code is as follows:
```
public int vowelsCount(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        } else if (c == 'y' && i == s.length() - 1) {
            count++;
        }
    }
    return count;
}
```
The time complexity of this solution is O(n), where n is the length of the input string, because it iterates through each character in the string once. The space complexity is O(1), because it uses a constant amount of space to store the counter.