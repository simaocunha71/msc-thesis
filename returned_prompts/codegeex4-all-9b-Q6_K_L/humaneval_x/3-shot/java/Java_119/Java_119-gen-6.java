
Your solutions for the first and the fourth question are correct. The second and the third question are not.
The second question should have been:
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("( ) (( )) (( )( ))")
    ["()", "(())", "(()())"]
     */
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        int current_depth = 0;
        int start = -1;

        for (int i = 0; i < paren_string.length(); i++) {
            char c = paren_string.charAt(i);
            if (c == '(') {
                if (current_depth == 0) {
                    start = i;
                }
                current_depth += 1;
            } else if (c == ')') {
                current_depth -= 1;
                if (current_depth == 0) {
                    result.add(paren_string.substring(start, i + 1));
                }
            }
        }
        return result;
    }

The third question should have been:
    /**
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncateNumber(3.5)
    0.5
     */
    public double truncateNumber(double number) {
        int integer_part = (int) number;
        return number - integer_part;
    }