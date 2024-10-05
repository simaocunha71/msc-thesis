        StringBuilder result = new StringBuilder();
        boolean space = false;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (space) {
                    result.append('-');
                    space = false;
                } else {
                    result.append('_');
                    space = true;
                }
            } else {
                result.append(c);
                space = false;
            }
        }

        return result.toString();
    }
}

