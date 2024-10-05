        List<String> result = new ArrayList<>();
        boolean found_whitespace = false;
        boolean found_comma = false;
        StringBuilder current_word = new StringBuilder();
        int lowercase_count = 0;

        for (char c : txt.toCharArray()) {
            if (Character.isWhitespace(c)) {
                found_whitespace = true;
                if (current_word.length() > 0) {
                    result.add(current_word.toString());
                    current_word.setLength(0);
                }
            } else if (c == ',') {
                found_comma = true;
                if (current_word.length() > 0) {
                    result.add(current_word.toString());
                    current_word.setLength(0);
                }
            } else {
                current_word.append(c);
            }
        }

        if (current_word.length() > 0) {
            result.add(current_word.toString());
        }

        if (found_whitespace) {
            return result;
        } else if (found_comma) {
            return result;
        } else {
            for (int i = 0; i < 26; i++) {
                if ((int) txt.charAt(i) >= 97 && (int) txt.charAt(i) <= 122) {
                    lowercase_count += 1;
                }
            }
            return lowercase_count % 2 != 0;
        }
    }
}

