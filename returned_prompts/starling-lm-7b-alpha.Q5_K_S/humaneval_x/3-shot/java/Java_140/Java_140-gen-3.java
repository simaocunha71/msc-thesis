        StringBuilder result = new StringBuilder();
        boolean space_seen = false;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (space_seen) {
                    result.append('-');
                } else {
                    result.append('_');
                }
                space_seen = true;
            } else {
                result.append(c);
                space_seen = false;
            }
        }
        return result.toString();
    }
}

