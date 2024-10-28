The problem statement is asking to check if a given string is "happy" or not. A string is considered "happy" if its length is at least 3 and every 3 consecutive letters are distinct.

Here is a Java solution for the problem:

```java
public boolean isHappy(String s) {
    if (s.length() < 3) return false;
    for (int i = 0; i < s.length() - 2; i++) {
        String threeChar = s.substring(i, i + 3);
        if (threeChar.length() == 3 && !isDistinct(threeChar)) {
            return false;
        }
    }
    return true;
}

private boolean isDistinct(String s) {
    Set<Character> set = new HashSet<>();
    for (char c : s.toCharArray()) {
        if (!set.add(c)) {
            return false;
        }
    }
    return true;
}
```

In this solution, we first check if the length of the string is less than 3. If it is, we return false because a string with a length less than 3 cannot be "happy".

Then we iterate over the string and for each 3 consecutive characters, we check if they are distinct using the `isDistinct` method. If we find a set of 3 consecutive characters that are not distinct, we return false.

The `isDistinct` method takes a string as input and returns a boolean indicating whether all characters in the string are distinct. It does this by converting the string to a character array and then using a HashSet to add each character to the set. If the set already contains a character when we try to add it, it means that the character is not distinct and we return false. If we can add all characters to the set without any duplicates, we return true.

If we finish iterating over the string and haven't found any sets of 3 consecutive characters that are not distinct, we return true, indicating that the string is "happy". Q.E.D. 