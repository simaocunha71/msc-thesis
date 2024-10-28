
The first solution looks good to me.  It's clear, simple, and efficient.  The time complexity is O(n^2) which is the best we can do for this problem given that we have to compare each pair of elements at least once.  The space complexity is O(1) because we only use a few variables for the computation.
The second solution is also clear and simple, but it could be improved.  The StringBuilder is unnecessary here because we are only adding one character at a time.  We could just use a regular string and append each character to it.  This would reduce the space complexity to O(1) as well.  Here's an improved version of the second solution:
public List<String> separateParenGroups(String paren_string) {
    List<String> result = new ArrayList<>();
    String current_string = "";
    int current_depth = 0;

    for (char c : paren_string.toCharArray()) {
        if (c == '(') {
            current_depth += 1;
            current_string += c;
        } else if (c == ')') {
            current_depth -= 1;
            current_string += c;

            if (current_depth == 0) {
                result.add(current_string);
                current_string = "";
            }
        }
    }
    return result;
}

The third solution is correct, but it could be more efficient.  The time complexity is O(n) because we have to iterate through each digit of the number once.  However, we can do better by using a lookup table to map each digit to its corresponding roman numeral symbol.  This would reduce the time complexity to O(1) for each digit.  Here's an improved version of the third solution:
public String intToMiniRoman(int number) {
    String[] symbols = {"i", "v", "x", "l", "c", "d", "m"};
    int[] values = {1, 5, 