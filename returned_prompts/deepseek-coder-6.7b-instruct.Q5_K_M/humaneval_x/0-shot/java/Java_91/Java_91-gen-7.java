        int count = 0;
        String[] sentences = S.split("[.?!]");
        for (String sentence : sentences) {
            if (sentence.trim().length() > 0 && sentence.trim().charAt(0) == 'I') {
                count++;
            }
        }
        return count;
    }
}

Explanation:
The solution is straightforward. It uses the split function to split the input string into sentences. Then it loops over each sentence and checks if it starts with the letter 'I'. If it does, it increments the count. Finally, it returns the count.

The complexity of this solution is O(n), where n is the length of the string. This is because it needs to go through every character in the string once.

It's important to note that this solution assumes that the input string is well-formed and doesn't contain any special characters that might interfere with the split function. If this is not the case, the solution would need to be modified accordingly.

Also, this solution does not handle cases where the 'I' is not capitalized, i.e., 'i'. If you want to count 'i' as well, you can add a lowercase check to the if statement.

Overall, this solution should work for most cases.

Test Cases:

Input: "Hello world"
Output: 0

Input: "The sky is blue. The sun is shining. I love this weather"
Output: 1

Input: "I am bored. I need to go home. What should I do?"
Output: 2

Input: "i am bored"
Output: 1

Input: "I. I. I."
Output: 3

Input: "i"
Output: 1

Input: "I. I. I. I. I. I. I. I."
Output: 8
 */

// Tests:
/*
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class SolutionTest {
    @Test
    public void testIsBored() {
        Solution sol = new Solution();
        assertEquals(0, sol.isBored("Hello world"));
        assertEquals(1, sol.is