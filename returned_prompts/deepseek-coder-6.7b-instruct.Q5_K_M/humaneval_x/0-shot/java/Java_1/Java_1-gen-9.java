        List<String> result = new ArrayList<>();
        int start = 0;
        int count = 0;
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                count++;
            } else if (paren_string.charAt(i) == ')') {
                count--;
                if (count == 0) {
                    result.add(paren_string.substring(start, i + 1));
                    start = i + 1;
                }
            }
        }
        return result;
    }
}

Explanation:
This solution works by iterating through the string and counting the number of open parentheses (incrementing count by one each time) and closed parentheses (decrementing count by one each time). When count reaches zero, we know we have found a group of balanced parentheses and we can add it to the result list. We also keep track of the start index of each group so we can use substring to extract it from the original string.

Time Complexity: O(n), where n is the length of the input string. We go through the string once.
Space Complexity: O(n), where n is the number of groups of balanced parentheses in the input string. We store each group in the result list.
*/

// Test cases
Solution sol = new Solution();
System.out.println(sol.separateParenGroups("(  )  (( ))  (( )( ))")); // ["()", "(())", "(()())"]
System.out.println(sol.separateParenGroups("()  (()) ((()))")); // ["()", "(())", "((()))"]
System.out.println(sol.separateParenGroups("((())) () (()()) (()) ()")); // ["((()))", "()", "(()())", "(())", "()"]
System.out.println(sol.separateParenGroups("")); // []
System.out.println(sol.separateParenGroups("((())) ((()))")); // ["((()))", "((()))"]

// Note: The above code is