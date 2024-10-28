        StringBuilder result = new StringBuilder();
        boolean space_seen = false;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                space_seen = true;
                result.append("_");
            } else if (space_seen) {
                result.append("-");
                space_seen = false;
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

