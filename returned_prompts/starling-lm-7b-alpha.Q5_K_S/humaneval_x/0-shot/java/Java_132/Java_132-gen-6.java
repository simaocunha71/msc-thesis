        int len = string.length();
        char[] chars = string.toCharArray();
        int open = 0;
        for (int i = 0; i < len; i++) {
            if (chars[i] == '[') {
                open++;
            } else if (chars[i] == ']') {
                open--;
            }
            if (open < 0) {
                break A;
            }
        }
        return open == 0;
    }
}


























```
