        int open = 0, close = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '<') open++;
            else close++;

            if (close > open) return false;
        }
        return close == open;
    }
}

