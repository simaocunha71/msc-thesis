        int maxStrength = Integer.MIN_VALUE;
        String strongestExtension = "";

        for (String extension : extensions) {
            int cap = 0;
            int sm = 0;

            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }

            int strength = cap - sm;

            if (strength > maxStrength) {
                maxStrength = strength;
                strongestExtension = extension;
            }
        }

        return class_name + "." + strongestExtension;
    }
}

This solution works by iterating through each extension, counting the number of uppercase and lowercase letters, and then calculating the strength as the difference between these two counts. The strongest extension is the one with the highest strength. If there are multiple extensions with the same highest strength, the one that comes first in the list is chosen.

The time complexity of this solution is O(n*m), where n is the number of extensions and m is the average length of the extensions. This is because we need to iterate through each extension and character in each extension. The space complexity is O(1), since we only store a constant number of variables.
    */
}

//src/main/java/com/codingtest/coderpad/solution/Solution2.java
package com.codingtest.coderpad.solution;

import java.util.*;
import java.lang.*;

class Solution2 {
    /**
    Given a string containing uppercase letters, you need to find if it's possible to rearrange the string such that no two adjacent characters are the same.
    If it's possible, return a possible rearrangement of the string. If it's not possible, return "".
    Example:
    for rearrange("AABC") == "ABAC"
    for rearrange("AABC") == ""
    */
    public String rearrange(String str) {
        int[] count = new int[26];
        int[] pos = new int[26];
        int