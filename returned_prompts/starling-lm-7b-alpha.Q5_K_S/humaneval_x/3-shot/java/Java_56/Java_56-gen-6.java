        int left_count = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                left_count += 1;
            } else if (c == '>') {
                left_count -= 1;
                if (left_count < 0) return false;
            }
        }
        return left_count == 0;
    }
}

