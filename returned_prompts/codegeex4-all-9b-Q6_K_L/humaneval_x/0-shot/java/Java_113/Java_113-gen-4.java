import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i"th string of the input.

    >>> oddCount(Arrays.asList("1234567"))
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> oddCount(Arrays.asList("3","11111111"))
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
     */
    public List<String> oddCount(List<String> lst) {
        List<String> output = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if (Character.isDigit(c) && (c - '0') % 2 != 0) {
                    count++;
                }
            }
            String result = "the number of odd elements " + count + "n the str" + count + "ng " + count + " of the " + count + "nput.";
            output.add(result);
        }
        return output;
    }
}