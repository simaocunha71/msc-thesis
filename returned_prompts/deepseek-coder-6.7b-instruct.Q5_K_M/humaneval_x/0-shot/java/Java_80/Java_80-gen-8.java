Here is the solution:

```java
class Solution {
    public boolean isHappy(String s) {
        if(s.length() < 3) {
            return false;
        }
        for(int i = 2; i < s.length(); i++) {
            if(s.charAt(i) == s.charAt(i-1) || s.charAt(i) == s.charAt(i-2) || s.charAt(i-1) == s.charAt(i-2)) {
                return false;
            }
        }
        return true;
    }
}
```

In this code, I check every 3 consecutive characters and see if they are all distinct. If they are, the string is happy and I return true. If not, the string is not happy and I return false. If the string is less than 3 characters long, I also return false.

I use the `charAt` method to access each character in the string. This method takes an integer as an argument, which is the index of the character to access. In this case, I use it to access each of the three consecutive characters.

The `||` operator is a logical OR operator. It returns true if either of the conditions on its left or right is true. In this case, I use it to check if any two of the three characters are the same. If they are, the string is not happy, so I return false.

The `<` operator is a less than operator. It returns true if the value on its left is less than the value on its right. In this case, I use it to check if the length of the string is less than 3. If it is, the string is not happy, so I return false.

Finally, if none of the above conditions are met, the string must be happy, so I return true.
