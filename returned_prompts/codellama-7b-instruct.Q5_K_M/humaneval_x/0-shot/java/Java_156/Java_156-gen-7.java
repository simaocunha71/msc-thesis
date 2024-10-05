import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> intToMiniRoman(19) == "xix"
    >>> intToMiniRoman(152) == "clii"
    >>> intToMiniRoman(426) == "cdxxvi"
     */
    public String intToMiniRoman(int number) {

        // Convert to string
        String s = String.valueOf(number);

        // Create a string builder
        StringBuilder sb = new StringBuilder();

        // Loop through each character
        for (int i = 0; i < s.length(); i++) {

            // Get current character
            char c = s.charAt(i);

            // Add to string builder
            sb.append(c);

            // If the current character is a 4 or 9
            if (c == '4' || c == '9') {

                // Add the next character to the string builder
                sb.append(s.charAt(i + 1));

                // Skip the next character
                i++;
            }
        }

        // Return the string builder as a string
        return sb.toString();
    }
}
