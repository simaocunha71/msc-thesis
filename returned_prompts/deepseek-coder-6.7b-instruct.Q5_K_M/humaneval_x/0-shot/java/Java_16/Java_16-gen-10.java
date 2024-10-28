        Set<Character> charSet = new HashSet<Character>();

        for (int i = 0; i < string.length(); i++) {
            charSet.add(Character.toLowerCase(string.charAt(i)));
        }

        return charSet.size();
    }
}

The solution uses a HashSet to store the distinct characters. The HashSet automatically removes any duplicates. We convert all characters to lower case before adding them to the set.

This solution has a time complexity of O(n), where n is the length of the string. The space complexity is also O(n) due to the space required by the HashSet.

The HashSet is used because it provides constant time performance for the basic operations like add, remove and contains.

It's also worth noting that this solution assumes that the input string is ASCII encoded. If the string can contain unicode characters, we would need to use a Unicode-aware approach to handle the characters.
*/




public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.countDistinctCharacters("xyzXYZ")); // should print 3
        System.out.println(sol.countDistinctCharacters("Jerry")); // should print 4
    }
}

// This is the main class to test the Solution class
// The main function tests the countDistinctCharacters method of the Solution class.
// The results are printed to the standard output.
// If the results are correct, you will see the expected output.
// If the results are incorrect, you will see different output.
// The correct output is 3 for "xyzXYZ" and 4 for "Jerry".
// The countDistinctCharacters method should return the correct number of distinct characters in the string, regardless of case.
// The method should ignore any characters that are not letters.
// If the string is empty, the method should return 0.
// If the string contains all the same characters, the method should return 1.
// If the string is null, the method should throw a NullPointerException.
// The method should work correctly with any string that contains letters,