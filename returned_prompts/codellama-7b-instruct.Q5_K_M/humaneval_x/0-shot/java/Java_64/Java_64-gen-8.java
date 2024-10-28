import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function vowelsCount which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowelsCount("abcde")
    2
    >>> vowelsCount("ACEDY")
    3
     */
    public int vowelsCount(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || (ch == 'y' && i == s.length() - 1)) {
                count++;
            }
        }
        return count;
    }

    /**
     * 
     * @param num: an integer
     * @return: the reverse of integer
     */
    public int reverseInteger(int num) {
        if (num == 0) {
            return 0;
        }
        int result = 0;
        while (num != 0) {
            result = result * 10 + num % 10;
            num = num / 10;
        }
        return result;
    }

    /**
     * 
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers(int[] A) {
        Arrays.sort(A);
    }

    /**
     * 
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers2(int[] A) {
        // write your code here
        Arrays.sort(A, (a, b) -> (a - b));
    }

    /**
     * 
    