        StringBuilder result = new StringBuilder();
        int spacesCount = 0;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                spacesCount += 1;
                if (spacesCount == 2) {
                    result.append('-');
                    spacesCount = 1;
                }
            } else {
                if (spacesCount > 0) {
                    result.append('_');
                    spacesCount = 0;
                }
                result.append(c);
            }
        }
        if (spacesCount == 2) {
            result.append('-');
        }
        return result.toString();
     }
}

