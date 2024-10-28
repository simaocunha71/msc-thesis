
Your solution for hasCloseElements is correct, but not optimal. You can reduce the complexity from O(n^2) to O(n) by sorting the list and checking the difference between adjacent elements:
import java.util.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        Collections.sort(numbers);
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) - numbers.get(i - 1) < threshold) return true;
        }
        return false;
    }
}

Your solution for separateParenGroups is also correct, but it can be simplified by using a stack to keep track of the current depth:
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;
        Stack<Integer> stack = new Stack<>();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
                stack.push(current_depth);
            } else if (c == ')') {
                current_depth -= 1;
                current_string.append(c);

                if (current_depth == 0) {
                    result.add(current_string.toString());
                    current_string.setLength(0);
                    stack.clear();
                }
            }
        }
        return result;
    }
}

Your solution for truncateNumber is correct, but it can be simplified by using the Math.floor method:
import java.util.*;

class Solution {
    public double truncateNumber(double number) {
        return number - Math.floor(number);
    }
}

Your solution for anyInt is correct, but it can be simplified by using the instanceof operator to check if the objects are integers:
import java.util.*;

class Solution {
    public boolean anyInt(Object x, Object y, Object z) {
        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) return false;
       