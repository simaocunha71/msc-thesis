```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Check if two words have the same characters.
    >>> sameChars("eabcdzzzz", "dddzzzzzzzddeddabc")
    true
    >>> sameChars("abcd", "dddddddabc")
    true
    >>> sameChars("dddddddabc", "abcd")
    true
    >>> sameChars("eabcd", "dddddddabc")
    false
    >>> sameChars("abcd", "dddddddabce")
    false
    >>> sameChars("eabcdzzzz", "dddzzzzzzzddddabc")
    false
     */
    public boolean sameChars(String s0, String s1) {
        return s0.chars().sorted().collect(StringBuffer::new, StringBuffer::appendCodePoint, StringBuffer::append).toString().equals(
            s1.chars().sorted().collect(StringBuffer::new, StringBuffer::appendCodePoint, StringBuffer::append).toString());
    }
}
```