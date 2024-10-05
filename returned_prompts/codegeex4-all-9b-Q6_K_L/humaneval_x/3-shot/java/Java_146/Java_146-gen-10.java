
The first question has an O(n^2) solution, which is unnecessary. You can solve it in O(n) by using a TreeSet. TreeSet is a set that automatically sorts its elements. With TreeSet, you can find the closest elements in O(log n). Here is the code:
import java.util.*;
import java.lang.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        TreeSet<Double> set = new TreeSet<>(numbers);
        for (Double num : numbers) {
            Double higher = set.higher(num);
            Double lower = set.lower(num);
            if ((higher != null && higher - num < threshold) || (lower != null && num - lower < threshold)) {
                return true;
            }
        }
        return false;
    }
}

The second question is a classic problem of parsing nested parentheses. It can be solved in O(n) using a stack. Here is the code:
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        StringBuilder current_string = new StringBuilder();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                stack.push(current_string.length());
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    throw new IllegalArgumentException("Unbalanced parentheses");
                }
                int start = stack.pop();
                current_string.setLength(start);
                result.add(current_string.toString());
            }
            current_string.append(c);
        }

        if (!stack.isEmpty()) {
            throw new IllegalArgumentException("Unbalanced parentheses");
        }

        return result;
    }
}

The third question can be solved using a simple