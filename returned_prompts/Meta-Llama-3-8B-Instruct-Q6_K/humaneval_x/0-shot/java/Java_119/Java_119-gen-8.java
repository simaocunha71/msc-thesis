    public String matchParens(List<String> lst) {
        int open = 0, close = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open++;
                } else if (c == ')') {
                    close++;
                }
            }
        }
        if (open == close) {
            return "Yes";
        } else {
            return "No";
        }
    }  //Time complexity is O(n*m) where n is the number of strings and m is the length of each string


