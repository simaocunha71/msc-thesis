        int count_opening = 0;
        int count_closing = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                count_opening += 1;
            } else if (c == '>') {
                count_closing += 1;
            }
        }
        return count_opening == count_closing;
    }
}

