import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> stringSequence(0)
    "0"
    >>> stringSequence(5)
    "0 1 2 3 4 5"
     */
    public String stringSequence(int n) {
        // Write your code here
        // String result = "";
        // for (int i = 0; i <= n; i++) {
        //     result += (i + " ");
        // }
        // return result;
        return String.join(" ", 
            new ArrayList<String>(
                IntStream.range(0, n + 1)
                .mapToObj(x -> String.valueOf(x))
                .collect(Collectors.toList())
            )
        );
    }
}

