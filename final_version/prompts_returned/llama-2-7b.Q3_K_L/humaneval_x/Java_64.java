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
        Set<Character> vowels = new HashSet<>();
        for (char ch :s.toLowerCase().toCharArray()) {
            if (ch >= 'a' && ch <= 'z') {
                vowels.add('a' + ch); //'a' + 'c' + 'd' etc.
            } else {
                switch(ch) {
                    case 'A':
                        return 1;
                    case 'E':
                        return 1;
                    case 'I':
                        return 1;
                    case 'O':
                        return 1;
                    case 'U':
                        return 1;
                }
            }
        }
        return vowels.size();
    }
}