        List<String> groups = new ArrayList<>();
        int start = 0;
        int openCount = 0;
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                if (openCount == 0) {
                    start = i;
                }
                openCount++;
            } else if (paren_string.charAt(i) == ')') {
                openCount--;
                if (openCount == 0) {
                    groups.add(paren_string.substring(start, i + 1));
                }
            }
        }
        return groups;
    }
}

This code works by iterating over the string, keeping track of the number of open parentheses. When it encounters a closed parenthesis, it decrements the count. When it encounters an open parenthesis and the count is 0, it sets the start of a new group. When it encounters a closed parenthesis and the count is 0, it adds the new group to the list of groups.

The time complexity of this code is O(n), where n is the length of the string. The space complexity is also O(n) because in the worst case (when all groups are balanced and not nested), we might end up storing all n characters in the list.
