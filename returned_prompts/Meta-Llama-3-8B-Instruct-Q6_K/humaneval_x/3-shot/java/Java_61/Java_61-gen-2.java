        int open = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '(') open++;
            else if (c == ')') {
                if (open == 0) return false;
                open--;
            }
        }
        return open == 0;
    }
}

