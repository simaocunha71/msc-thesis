        int open = 0, close = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') open++;
            else if (c == ']') close++;
            if (open == 0 && close > 0) return true;
        }
        return false;
    }
}

