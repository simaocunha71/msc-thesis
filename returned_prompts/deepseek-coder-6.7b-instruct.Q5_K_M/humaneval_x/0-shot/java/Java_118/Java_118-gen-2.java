        StringBuilder sb = new StringBuilder();
        String vowels = "aeiouAEIOU";
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
        int length = word.length();
        for (int i = length - 2; i > 0; i--) {
            if (vowels.contains(String.valueOf(word.charAt(i))) &&
                    consonants.contains(String.valueOf(word.charAt(i - 1))) &&
                    consonants.contains(String.valueOf(word.charAt(i + 1)))) {
                sb.append(word.charAt(i));
                break;
            }
        }
        return sb.toString();
    }
}

The solution is a function that takes in a string and returns the closest vowel between two consonants. If no such vowel exists, it returns an empty string. The function checks the string from the end to the beginning, and when it finds a vowel between two consonants, it stops and returns the vowel.

Here is how it works:

1. Create a StringBuilder to store the result.
2. Define the vowels and consonants.
3. Iterate over the string from the end to the beginning.
4. Inside the loop, check if the current character is a vowel and the characters before and after it are consonants.
5. If the condition is met, append the character to the StringBuilder and break the loop.
6. Return the result as a string.

This solution has a time complexity of O(n), where n is the length of the string.
    */
}﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solution
{
    public class Solution
    {
        public string solve(string s)
        {
            return string.Concat(s.GroupBy(c => c).OrderBy(g => g.Count()).Select(g => g.Key));
        }
    }
}

//The solution