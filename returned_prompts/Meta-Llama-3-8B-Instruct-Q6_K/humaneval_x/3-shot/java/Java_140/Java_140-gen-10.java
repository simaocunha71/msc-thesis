        StringBuilder result = new StringBuilder();
        int i = 0;

        while (i < text.length()) {
            if (text.charAt(i) == ' ') {
                if (i + 1 < text.length() && text.charAt(i + 1) == ' ') {
                    result.append('-');
                    i += 1;
                } else {
                    result.append('_');
                }
            } else {
                result.append(text.charAt(i));
            }
            i += 1;
        }
        return result.toString();
    }
}

