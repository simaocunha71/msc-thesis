Here's the corrected version of your code:

import java.util.*;
import java.lang.*;

class Solution 
{
    /**
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") ➞ 0
        digitSum("abAB") ➞ 131
        digitSum("abcCd") ➞ 67
        digitSum("helloE") ➞ 69
        digitSum("woArBld") ➞ 131
        digitSum("aAaaaXa") ➞ 153
      */
    public int digitSum(String s) 
    {
        int sum = 0;
        for(int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if(Character.isUpperCase(c))
            {
                sum += (int) c;
            }
        }
        return sum;
    }
}

This code works by iterating over each character in the given string `s`. If the character is uppercase (checked with the `Character.isUpperCase(c)` function), its ASCII value is added to the sum. This is done by casting the character to an integer using `(int) c`.

Finally, the sum of the ASCII values of the uppercase characters in the string is returned.

This is an appropriate solution because it correctly calculates the sum of ASCII values of uppercase characters in a string.

Also, the comments in the code are formatted correctly, so there should be no issues with the code being executed.
