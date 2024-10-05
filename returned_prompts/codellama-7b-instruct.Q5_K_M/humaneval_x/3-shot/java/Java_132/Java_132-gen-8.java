        int left_count = 0;
        int right_count = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') left_count += 1;
            if (c == ']') right_count += 1;
        }
        return left_count > right_count;
    }
}

