        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");

        for (String group : groups) {
            int count = 0;
            int max = 0;

            for (char c : group.toCharArray()) {
                if (c == '(') {
                    count++;
                    if (count > max) {
                        max = count;
                    }
                } else if (c == ')') {
                    count--;
                }
            }

            result.add(max);
        }

        return result;
    }
}

Explanation:
This solution works by iterating over each character in the string. It counts the number of open parentheses and keeps track of the maximum count. The maximum count is the maximum depth of nesting. This is done for each group of parentheses in the input string. The results are stored in a list and returned.

Complexity Analysis:
The time complexity is O(n) where n is the number of characters in the input string. This is because each character is visited exactly once. The space complexity is O(m) where m is the number of groups in the input string. This is because each group is processed and a result is stored in the results list.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> result = solution.parseNestedParens("(()()) ((())) () ((())()())");
        System.out.println(result); // Expected output: [2, 3, 1, 3]
    }
}


































































































































