    boolean isSubString = false;

B:
    for (int i = 0; i < b.length(); i++) {

C:
        String rotated = b.substring(i) + b.substring(0, i);

D:
        if (a.contains(rotated)) {
            isSubString = true;
            break;
        }
    }

E:
    return isSubString;
    }
}

Answer:
A: The variable `isSubString` is used to check whether the second word or any of its rotations is a substring in the first word.

B: The loop iterates through every possible rotation of the second word `b`.

C: The `rotated` variable holds the rotated version of the second word at each iteration.

D: If the first word `a` contains `rotated`, `isSubString` is set to `true` and the loop breaks.

E: The function returns `isSubString`, which will be `true` if any rotation of the second word is a substring of the first word, and `false` otherwise.

The time complexity of the algorithm is O(n*m) where n is the length of the first word and m is the length of the second word, because in the worst case, we are checking if the first word contains each rotation of the second word.

The space complexity is O(n) because we are storing each rotation of the second word in a separate String variable.
*/


import java.util.*;
import java.lang.*;

class Solution  {
    public boolean cycpatternCheck(String a, String b) {
        boolean isSubString = false;
        for (int i = 0; i < b.length(); i++) {
            String rotated = b.substring(i) + b.substring(0, i);
            if (a.contains(rotated)) {
                isSubString = true;
                break;
            }
        }
        return isSubString;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(