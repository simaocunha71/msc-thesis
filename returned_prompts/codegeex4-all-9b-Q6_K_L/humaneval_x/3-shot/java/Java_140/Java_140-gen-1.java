        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == ' ') {
                int consecutive_spaces = 0;

                while (i < text.length() && text.charAt(i) == ' ') {
                    consecutive_spaces += 1;
                    i += 1;
                }

                i -= 1;

                if (consecutive_spaces == 1) {
                    result.append("_");
                } else if (consecutive_spaces >= 2) {
                    result.append("-");
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

