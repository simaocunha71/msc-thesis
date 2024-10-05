        int result = 0;
        StringBuilder current_word = new StringBuilder();
        boolean is_boredom = false;

        for (char c : S.toCharArray()) {
            if (c == '.') {
                is_boredom = false;
                current_word.setLength(0);
            } else if (c == '?') {
                is_boredom = false;
                current_word.setLength(0);
            } else if (c == '!') {
                is_boredom = false;
                current_word.setLength(0);
            } else if (c == 'I') {
                is_boredom = true;
                current_word.append(c);
            } else {
                current_word.append(c);
            }

            if (is_boredom && !current_word.toString().isEmpty()) {
                result += 1;
            }
        }
        return result;
    }
}

