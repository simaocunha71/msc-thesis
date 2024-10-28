    if(isPalindrome(string)){
        return string;
    }
    int len = string.length();
    for(int i = len; i >= 0; i--){
        if(isPalindrome(string.substring(0, i))){
            StringBuilder sb = new StringBuilder(string.substring(0, len - i));
            return string + sb.reverse().toString();
        }
    }
    return null;
}
}

```

## Test Cases
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {
    Solution sol = new Solution();

    @Test
    void isPalindromeTest(){
        assertEquals(true, sol.isPalindrome(""));
        assertEquals(true, sol.isPalindrome("a"));
        assertEquals(true, sol.isPalindrome("aa"));
        assertEquals(true, sol.isPalindrome("aba"));
        assertEquals(false, sol.isPalindrome("ab"));
    }

    @Test
    void makePalindromeTest(){
        assertEquals("", sol.makePalindrome(""));
        assertEquals("a", sol.makePalindrome("a"));
        assertEquals("aa", sol.makePalindrome("a"));
        assertEquals("aba", sol.makePalindrome("a"));
        assertEquals("abaa", sol.makePalindrome("ab"));
    }
}
```

## Code Explanation

The `isPalindrome` function checks if a given string is a palindrome or not. It does this by comparing characters from the start and end of the string and moving inwards. If it finds any mismatch it returns false, otherwise it returns true.

The `makePalindrome` function first checks if the string is already a palindrome. If so, it returns the string itself. Otherwise, it finds the longest postfix of the string that is a palindrome. It then appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix.

The JUnit test cases are for `isPalindrome` and `make