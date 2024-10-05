        List<Integer> result = new ArrayList<>();
        int level = 0;
        boolean open = false;
        int pos = 0;
        while (pos < paren_string.length()) {
            if (paren_string.charAt(pos) == '(') {
                if (open) {
                    level++;
                } else {
                    open = true;
                }
            } else {
                if (open && paren_string.charAt(pos) == ')') {
                    level--;
                } else {
                    open = false;
                }
            }
            pos++;
            if (pos == paren_string.length() && open) {
                level++;
            }
            result.add(level);
        }
        return result;
    }
}
