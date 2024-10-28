    public String matchParens(List<String> lst) {
        int countOpen = 0;
        int countClose = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    countOpen++;
                } else {
                    if (countOpen == 0) {
                        return "No";
                    }
                    countOpen--;
                    countClose++;
                }
            }
        }
        return countOpen == 0 ? "Yes" : "No";
    }
    The idea is to count the number of open and close parentheses. If at any point we see a close parenthesis without an open parenthesis to match it, we return "No". If after going through all the strings, we still have open parentheses left, it means that we don't have enough close parentheses to match them, so we return "No". Otherwise, we return "Yes". This is because we can always match the open and close parentheses one by one, and if we can do that, then the string is good. .


    Time Complexity: O(n*m)
    Space Complexity: O(1)
    where n is the number of strings and m is the maximum length of a string.