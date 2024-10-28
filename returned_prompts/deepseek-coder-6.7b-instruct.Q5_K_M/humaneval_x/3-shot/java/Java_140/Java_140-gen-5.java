        StringBuilder result = new StringBuilder();
        boolean prevWasSpace = false;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (prevWasSpace) {
                    result.append('-');
                } else {
                    result.append('_');
                }
                prevWasSpace = true;
            } else {
                result.append(c);
                prevWasSpace = false;
            }
        }
        return result.toString();
     }
}

