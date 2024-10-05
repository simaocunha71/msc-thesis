        StringBuilder result = new StringBuilder();
        boolean hasConsecutiveSpace = false;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (hasConsecutiveSpace) {
                    result.append('-');
                } else {
                    result.append('_');
                    hasConsecutiveSpace = true;
                }
            } else {
                result.append(c);
                hasConsecutiveSpace = false;
            }
        }

        return result.toString();
    }
}

