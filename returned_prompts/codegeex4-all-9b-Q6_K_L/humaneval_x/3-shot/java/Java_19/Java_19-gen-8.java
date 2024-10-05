
You have a few issues with your code. The first thing I'd like to point out is that you're missing the @Test annotations which are used to test the functions you're writing. The second issue is that you're not properly closing your HTML tags, and the third issue is that your functions aren't properly formatted to be able to be tested properly. 

Here's the corrected code:

```java
import org.junit.Test;

import java.util.*;

public class Solution {

    @Test
    public void testHasCloseElements() {
        List<Double> numbers1 = Arrays.asList(1.0, 2.0, 3.0);
        List<Double> numbers2 = Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0);
        double threshold = 0.5;
        assert !hasCloseElements(numbers1, threshold);
        assert hasCloseElements(numbers2, threshold);
    }

    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
        return false;
    }

    @Test
    public void testSeparateParenGroups() {
        String paren_string = "( ) (( )) (( )( ))";
        List<String> expected = Arrays.asList("()", "(())", "(()())");
        assert separateParenGroups(paren_string).equals(expected);
    }

    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
            } else if (c == ')') {
                current_depth -= 1;
                current_string.append(c);

                if (current_depth == 0) {
                    result.add(current_string.toString());
                    current_string.setLength(0);
                }
            }
        }
        return result;
    }

    @Test
    public