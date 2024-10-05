        StringBuilder sb = new StringBuilder();
        char prev = ' ';
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (prev == ' ') {
                    sb.append('-');
                } else {
                    sb.append('_');
                }
                prev = c;
            } else {
                sb.append(c);
                prev = c;
            }
        }
        return sb.toString();
    }
}

