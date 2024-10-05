        int vowelCount = 0;
        String vowels = "aeiou";

        for (int i = 0; i < s.length(); i++) {
            if (vowels.contains(Character.toString(s.charAt(i)).toLowerCase())) {
                vowelCount++;
            }
        }

        if (s.charAt(s.length() - 1) == 'y') {
            vowelCount++;
        }

        return vowelCount;
    }
}

This solution loops through the string and checks if the current character is a vowel (ignoring case). If it is, it increments the vowel count. Finally, if the last character of the string is 'y', it increments the vowel count. The result is the total number of vowels in the string.

The time complexity of this solution is O(n), where n is the length of the string. This is because we are looping through the string once. The space complexity is O(1), as we are using a constant amount of space to store the vowel count and the vowel string.

*/

public class Main {
    public static void main(String[] args) {
        Solution soln = new Solution();
        System.out.println(soln.vowelsCount("abcde"));
        System.out.println(soln.vowelsCount("ACEDY"));
    }
}

//src/main/java/com/company/problems/strings/VowelsInString.java
package com.company.problems.strings;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class VowelsInString {

    public static void main(String[] args) {
        System.out.println(countVowels("hello"));
    }

    public static int countVowels(String str) {
        // a, e, i, o, u
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        int count = 0;
        for(int i = 