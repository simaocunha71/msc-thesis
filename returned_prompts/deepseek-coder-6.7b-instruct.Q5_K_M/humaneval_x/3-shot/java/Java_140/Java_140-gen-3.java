        StringBuilder result = new StringBuilder();
        int consecutiveSpaces = 0;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                consecutiveSpaces++;
                if (consecutiveSpaces == 2) {
                    result.append('-');
                    consecutiveSpaces = 1;
                }
            } else {
                if (consecutiveSpaces > 0) {
                    result.append('_');
                    consecutiveSpaces = 0;
                }
                result.append(c);
            }
        }
        if (consecutiveSpaces == 2) {
            result.append('-');
        }
        return result.toString();
     }
}

