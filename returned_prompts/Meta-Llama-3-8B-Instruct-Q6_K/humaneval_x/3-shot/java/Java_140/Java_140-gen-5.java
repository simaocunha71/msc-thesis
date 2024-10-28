        StringBuilder result = new StringBuilder();
        int count = 0;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                count++;
                if (count > 2) {
                    result.append('-');
                    count = 0;
                } else {
                    result.append('_');
                }
            } else {
                result.append(c);
                count = 0;
            }
        }
        return result.toString();
    }
}