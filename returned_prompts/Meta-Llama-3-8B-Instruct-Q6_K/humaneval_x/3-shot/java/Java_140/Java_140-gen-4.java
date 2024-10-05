        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                if (result.length() > 0 && result.charAt(result.length() - 1) == ' ') {
                    if (result.length() > 1) {
                        result.append('-');
                    }
                } else {
                    result.append('_');
                }
            } else {
                result.append(text.charAt(i));
            }
        }
        return result.toString();
    }
}

