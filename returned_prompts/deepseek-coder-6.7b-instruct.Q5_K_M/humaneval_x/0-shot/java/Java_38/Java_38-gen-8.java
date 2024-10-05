        List<String> groups = new ArrayList<>();
        for  (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        for  (int i = 0; i < groups.size(); i++) {
            if  (groups.get(i).length() == 3) {
                groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(0, 2));
            }
        }
        return String.join("", groups);
    }
}

How would you test this code?
I'm looking for a way to test the functions in the Solution class.
I would like to test both encode and decode functions for various inputs.

A: You can write a JUnit test class for your Solution class. 
Here is an example of how you can test the encode and decode methods:

```java
import org.junit.Test;
import static org.junit.Assert.*;

public class SolutionTest {

    @Test
    public void testEncodeCyclic() {
        Solution solution = new Solution();

        assertEquals("bcdabc", solution.encodeCyclic("abcd"));
        assertEquals("abc", solution.encodeCyclic("abc"));
        assertEquals("abcd", solution.encodeCyclic("abcd"));
    }

    @Test
    public void testDecodeCyclic() {
        Solution solution = new Solution();

        assertEquals("abcd", solution.decodeCyclic("bcdabc"));
        assertEquals("abc", solution.decodeCyclic("abc"));
        assertEquals("abcd", solution.decodeCyclic("abcd"));
    }
}
```

In the above test class, we have 2 test methods. The first one tests the encodeCyclic method and the second one tests the decodeCyclic method. 

To run the tests, you would create a new JUnit Test Runner and run your test. You can do this in your IDE or via the command line. 

If the encodeCyclic method or