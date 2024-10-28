        Stack<String> stack = new Stack<String>();
        List<String> result = new ArrayList<String>();
        StringBuilder sb = new StringBuilder();
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                sb.append(c);
                stack.push(sb.toString());
                sb = new StringBuilder();
            } else if (c == ')') {
                if (!stack.isEmpty()) {
                    String top = stack.pop();
                    if (top.charAt(top.length() - 1) == '(') {
                        result.add(top + c);
                    } else {
                        String poped = top + c;
                        if (!stack.isEmpty()) {
                            String temp = stack.pop();
                            result.add(poped + temp);
                        } else {
                            result.add(poped);
                        }
                    }
                } else {
                    sb.append(c);
                }
            } else {
                sb.append(c);
            }
        }
        return result;
    }
}



class Test {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.separateParenGroups("( ) (( )) (( )( ))"));
    }
}



















































































































































































