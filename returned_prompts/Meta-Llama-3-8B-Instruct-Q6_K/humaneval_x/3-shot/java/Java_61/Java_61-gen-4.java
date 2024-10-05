        int open = 0, close = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '(') open++;
            else close++;

            if (open < close) return false;
        }
        return open == close;
    }
}

