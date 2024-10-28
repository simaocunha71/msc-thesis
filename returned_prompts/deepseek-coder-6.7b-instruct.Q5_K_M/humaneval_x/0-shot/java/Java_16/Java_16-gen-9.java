        Set<Character> set = new HashSet<>();
        string = string.toLowerCase();
        for (int i = 0; i < string.length(); i++){
            set.add(string.charAt(i));
        }
        return set.size();
    }
}

This solution works by first converting the string to lower case, then looping through each character in the string and adding it to a HashSet. A HashSet in Java does not allow duplicate values, so the number of distinct characters is just the size of the HashSet.



*/

import java.util.*;
class Solution {
    public int countDistinctCharacters(String string) {
        Set<Character> set = new HashSet<>();
        string = string.toLowerCase();
        for (int i = 0; i < string.length(); i++){
            set.add(string.charAt(i));
        }
        return set.size();
    }
}


// Test cases
class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countDistinctCharacters("xyzXYZ"));  // Output: 3
        System.out.println(solution.countDistinctCharacters("Jerry"));  // Output: 4
    }
}

/*
Output: 
3
4
*/

/*
Time complexity: O(n) where n is the length of the string. 
Space complexity: O(1) as the maximum number of distinct characters is 26 (assuming English alphabet).
*/


// This solution does not consider spaces, punctuation and other special characters. 
// If you want to consider them, you need to add them into the character set.

// If you want to ignore case sensitivity, you can remove the line: string = string.toLowerCase();
// This will consider uppercase and lowercase letters as the same.

// If you want to count spaces as a character, you can add: set.add(' '); to the line: for (int i = 0; i < string.length(); i++){}
// This will count the number of distinct characters, including