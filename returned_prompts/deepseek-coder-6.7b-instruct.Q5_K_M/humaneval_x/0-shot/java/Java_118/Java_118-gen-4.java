        // your code here
    }
}


A: Here is a solution using Java:

```java
class Solution {
    public String getClosestVowel(String word) {
        String vowels = "aeiouAEIOU";
        for (int i = word.length() - 2; i > 0; i--) {
            if (vowels.indexOf(word.charAt(i)) != -1 && !vowels.contains(word.charAt(i-1) + "") && !vowels.contains(word.charAt(i+1) + "")) {
                return Character.toString(word.charAt(i));
            }
        }
        return "";
    }
}
```

This solution works by iterating over the characters of the string from right to left, skipping the first and last characters (since they can't be between two consonants). For each character, it checks if it is a vowel and if the characters on its left and right are not vowels. If it finds such a character, it returns it. If it doesn't find any, it returns an empty string.

Note that this solution is case-sensitive, as specified in the problem statement.

Also note that the `indexOf` function returns `-1` when the character is not found in the string.

And the `contains` method returns true if the string contains the specified sequence of char values.

The `Character.toString(char ch)` method returns a new String object that represents the specified char value.

Here is how you can use this function:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.getClosestVowel("yogurt"));  // prints "u"
    System.out.println(solution.getClosestVowel("FULL"));    // prints "U"
    System.out.println(solution.getClosestVowel("quick"));   // prints ""
    System.out.println(solution.getClosestVowel("ab"));      // prints ""
}
```

This will print the closest vow