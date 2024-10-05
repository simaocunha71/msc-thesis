    List<String> ans = new ArrayList<String>();
    Stack<Character> stack = new Stack<Character>();
    StringBuilder sb = new StringBuilder();

    for(int i = 0; i < paren_string.length(); i++) {
        char c = paren_string.charAt(i);

        if(c == '(') {
            stack.push(c);
        } else if(c == ')') {
            if(stack.isEmpty()) {
                ans.add(sb.toString());
                sb = new StringBuilder();
            } else {
                stack.pop();
            }
        } else {
            sb.append(c);
        }
    }

    if(!stack.isEmpty()) {
        ans.add(sb.toString());
    }

    return ans;
    }
}



class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("( ) (( )) (( )( ))")
    ["()", "(())", "(()())"]
     */
    public List<String> separateParenGroups(String paren_string) {

    List<String> ans = new ArrayList<String>();
    Stack<Character> stack = new Stack<Character>();
    StringBuilder sb = new StringBuilder();
    int i = 0;
    while(i < paren_string.length()) {
        char c = paren_string.charAt(i);

        if(c == '(') {
            stack.push(c);
        } else if(c == ')') {
            if(stack.isEmpty()) {
                ans.add(sb.toString());
                sb = new StringBuilder();
            } else {
                stack.pop();
            }
        } else {
            sb.append(c);
        }
        i++;
    }

    if(!stack.isEmpty()) {
        ans.add(