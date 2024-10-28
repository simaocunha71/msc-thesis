        StringBuilder result = new StringBuilder();
        boolean prevSpace = false;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (prevSpace) {
                    result.append('-');
                } else {
                    result.append('_');
                }
                prevSpace = true;
            } else {
                result.append(c);
                prevSpace = false;
            }
        }
        return result.toString();
    }
}

