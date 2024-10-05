        int count = 0;
        for(int i = 0; i < s.length(); i += 2){
            char c = s.charAt(i);
            if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
                count++;
            }
        }
        return count;
    }
}

// Test Cases
import java.util.Arrays;
public class TestCases {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.countUpper("aBCdEf") == 1);
        System.out.println(s.countUpper("abcdefg") == 0);
        System.out.println(s.countUpper("dBBE") == 0);
    }
}

*/

/*

Explanation:

The solution is quite straightforward. It loops through the string at every even index. If the character at that index is an uppercase vowel (A, E, I, O, U), it increments a counter. Finally, it returns the count.

The test cases check if the function correctly counts the uppercase vowels at even indices in a string.

*/

// Code Ends Here

// Test Cases
/*

import java.util.Arrays;
public class TestCases {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.countUpper("aBCdEf") == 1);
        System.out.println(s.countUpper("abcdefg") == 0);
        System.out.println(s.countUpper("dBBE") == 0);
    }
}

*/

/*

Explanation:

The solution is quite straightforward. It loops through the string at every even index. If the character at that index is an uppercase vowel (A, E, I, O, U), it increments a counter. Finally, it returns the count.

The test cases check if the function correctly counts the uppercase vowels at even indices in a string.

*/