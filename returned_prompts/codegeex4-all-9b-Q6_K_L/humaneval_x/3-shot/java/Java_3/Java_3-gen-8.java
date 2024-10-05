
For the first question, you could use a TreeSet instead of a List. It would automatically sort the numbers for you and keep only unique elements. Then you just have to iterate through the sorted list and see if any two adjacent numbers are closer than the threshold.
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        Set<Double> sorted = new TreeSet<>(numbers);
        Double previous = null;
        for (Double current : sorted) {
            if (previous != null && current - previous < threshold) {
                return true;
            }
            previous = current;
        }
        return false;
    }
}

The second question can be solved with a stack. You push each character to the stack and when you encounter a closing parenthesis, you pop from the stack until you find the matching opening parenthesis. If you reach the end of the string and the stack is not empty, then the parentheses are not balanced.
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                stack.push(c);
                current_string.append(c);
            } else if (c == ')') {
                current_string.append(c);
                while (!stack.isEmpty() && stack.peek() != '(') {
                    current_string.append(stack.pop());
                }
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                    if (stack.isEmpty()) {
                        result.add(current_string.toString());
                        current_string.setLength(0);
                    }
                } else {
                    current_string.setLength(0);
                }
            }
        }
        return result;
    }
}

The third question can be solved by using the modulo operator %. The result of n % 1.0 is always the fractional part of n.
import java.util.*;

class Solution {
    public double truncateNumber(double number) {
        return number % 1.0;
    }
}

The fourth question can be solved by using a simple loop and adding each operation to the balance. If the balance falls below zero, return true. Otherwise, return false.
import java