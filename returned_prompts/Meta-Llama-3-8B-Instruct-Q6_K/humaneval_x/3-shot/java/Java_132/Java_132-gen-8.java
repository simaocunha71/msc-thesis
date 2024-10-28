        int count = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                count++;
            } else if (c == ']') {
                count--;
                if (count < 0) {
                    return true;
                }
            }
        }
        return false;
    }
}

