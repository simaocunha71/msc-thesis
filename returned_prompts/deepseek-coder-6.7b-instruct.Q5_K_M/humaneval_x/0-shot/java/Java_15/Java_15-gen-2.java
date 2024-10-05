        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            sb.append(i);
            if(i < n) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }

}

This code will return a string containing space-delimited numbers starting from 0 upto n inclusive.

In the function stringSequence, we are creating a StringBuilder object sb and appending the numbers from 0 to n to it. We append a space after each number except the last one. We then return the string representation of the StringBuilder.
*/

import java.util.*;

class Main {
    public static void main (String[] args) {
        Solution s = new Solution();
        System.out.println(s.stringSequence(0));  // should print "0"
        System.out.println(s.stringSequence(5));  // should print "0 1 2 3 4 5"
    }
}



```

The code defines a class `Solution` with a method `stringSequence` that takes an integer `n` as input and returns a string containing numbers from 0 to `n` separated by spaces. 

The function works by creating a `StringBuilder` object `sb` and appending numbers from 0 to `n` to it. It also appends a space after each number except the last one. 

The resulting string is then returned.

The main method tests the `stringSequence` method by creating a `Solution` object and calling `stringSequence` method on it with the inputs 0 and 5. The results are printed to the console.

























































































































