        StringBuilder result = new StringBuilder();
        StringBuilder current_word = new StringBuilder();
        for (char c : s.toCharArray()) {
            current_word.append(c);
            if (c == ' ') {
                result.append(order(current_word.toString())).append(' ');
                current_word.setLength(0);
            }
        }
        result.append(order(current_word.toString()));
        return result.toString();
    }

    private String order(String s) {
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            result.append((char) (c + 1));
        }
        return result.toString();
    }
}




```