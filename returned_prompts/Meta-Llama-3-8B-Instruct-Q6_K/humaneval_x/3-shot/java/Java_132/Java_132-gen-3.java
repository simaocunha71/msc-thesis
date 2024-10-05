        int open_count = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                open_count++;
            } else if (c == ']') {
                open_count--;
                if (open_count < 0) return true;
            }
        }
        return false;
    }
}

