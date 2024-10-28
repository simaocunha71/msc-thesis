        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (result.length() > 0 && result.charAt(result.length() - 1) == ' ') {
                    result.append('-');
                } else {
                    result.append('_');
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

