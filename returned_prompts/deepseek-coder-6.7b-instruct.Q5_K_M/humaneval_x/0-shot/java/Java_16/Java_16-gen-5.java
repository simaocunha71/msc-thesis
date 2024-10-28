        Set<Character> uniqueChars = new HashSet<Character>();
        for (int i = 0; i < string.length(); i++) {
            uniqueChars.add(Character.toLowerCase(string.charAt(i)));
        }
        return uniqueChars.size();
    }
}

In this code, we are using a HashSet to keep track of the unique characters in the string. We convert each character to lowercase before adding it to the set to ensure that the function is case-insensitive. The size of the set at the end of the function is the number of distinct characters in the string.

This solution has a time complexity of O(n), where n is the length of the input string, because we are iterating through each character of the string once. The space complexity is also O(n), because in the worst case, each character in the string may end up in the set once.





*/

import java.util.*;
import java.lang.*;

class Solution  {
    public int countDistinctCharacters(String string) {
        Set<Character> uniqueChars = new HashSet<Character>();
        for (int i = 0; i < string.length(); i++) {
            uniqueChars.add(Character.toLowerCase(string.charAt(i)));
        }
        return uniqueChars.size();
    }
}

public class Main
{
	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.countDistinctCharacters("xyzXYZ")); // 3
		System.out.println(sol.countDistinctCharacters("Jerry")); // 4
	}
}
/*
Output:
3
4
*/

/*
Explanation:
In the first case, the distinct characters are 'x', 'y', 'z' and 'X', 'Y', 'Z'. So the answer is 3.
In the second case, the distinct characters are 'J', 'e', 'r', 'y'. So the answer is 4.
*/
























