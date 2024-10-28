        int opening_count = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '<') opening_count += 1;
            if (c == '>') opening_count -= 1;
        }
        return opening_count == 0;
    }
}

