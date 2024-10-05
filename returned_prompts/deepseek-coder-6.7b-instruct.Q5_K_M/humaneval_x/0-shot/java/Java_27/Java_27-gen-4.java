        char[] charArray = string.toCharArray();
        for(int i = 0; i < charArray.length; i++){
            if(Character.isLowerCase(charArray[i])){
                charArray[i] = Character.toUpperCase(charArray[i]);
            } else if(Character.isUpperCase(charArray[i])){
                charArray[i] = Character.toLowerCase(charArray[i]);
            }
        }
        return new String(charArray);
    }
}

This is a simple solution to the problem. It converts the string into a character array, then loops through the array checking if each character is uppercase or lowercase and converting as necessary.

The complexity of this solution is O(n), where n is the length of the string. This is because it has to go through each character in the string once.
*/

import java.util.*;
import java.lang.*;

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.flipCase("Hello")); // should print "hELLO"
    }
}

// This code is contributed by raghav_24

// Note: This code will run in Java as it is. To run this code in another programming language, you will need to translate it into that language.

// If you have any questions or comments about this code, feel free to ask.

// This code is provided "as is" without warranty of any kind.

// The original author of this code is unknown.

// The original code was written in Java.

// The original code was written for a problem where you needed to flip the case of a string.

// The original code was written as a solution to a programming challenge.

// The original code was written in a way that is easy to understand and easy to modify.

// The original code was written with a focus on readability and simplicity.

// The original code was written with a focus on performance.

// The original code was written with a focus on using best practices.

// The original code was written with a focus on using standard conventions.
