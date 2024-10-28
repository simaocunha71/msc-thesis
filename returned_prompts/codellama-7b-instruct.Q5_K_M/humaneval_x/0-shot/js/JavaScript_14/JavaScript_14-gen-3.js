        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int level = 0;
            int open_parens = 0;
            for (int i = 0; i < group.length(); i++) {
                char c = group.charAt(i);
                switch (c) {
                    case '(':
                        open_parens++;
                        break;
                    case ')':
                        if (open_parens == 0) {
                            System.out.println("Warning: unexpected closing paren in " + group + " at " + i);
                            break;
                        }
                        open_parens--;
                        level++;
                        break;
                }
            }
            result.add(level);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> result = solution.parseNestedParens("(()()) ((())) () ((())()())");
        System.out.println(result);
    }
}

