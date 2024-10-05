        StringBuilder result = new StringBuilder();
        boolean lastWasSpace = false;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (lastWasSpace) {
                    result.append('-');
                } else {
                    result.append('_');
                }
                lastWasSpace = true;
            } else {
                result.append(c);
                lastWasSpace = false;
            }
        }
        return result.toString();
    }
}

