        StringBuilder result = new StringBuilder();
        boolean had_space = false;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (!had_space) {
                    result.append('_');
                }
                had_space = true;
            } else {
                had_space = false;
                result.append(c);
            }
        }
        return result.toString();
    }
}

