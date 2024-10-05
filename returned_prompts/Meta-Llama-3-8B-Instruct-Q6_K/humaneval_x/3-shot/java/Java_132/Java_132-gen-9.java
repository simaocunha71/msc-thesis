        int open_count = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') open_count++;
            else if (c == ']') {
                if (open_count == 0) return true;
                open_count--;
            }
        }
        return false;
    }
}

