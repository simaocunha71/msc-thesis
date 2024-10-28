        StringBuilder sb = new StringBuilder(s);
        int first = -1;
        int last = -1;
        for (int i = 0; i < sb.length(); i++) {
            char c = sb.charAt(i);
            if (Character.isLetter(c)) {
                if (first == -1) {
                    first = i;
                }
                last = i;
            }
        }
        if (first != -1) {
            for (int i = first; i <= last; i++) {
                char c = sb.charAt(i);
                if (Character.isUpperCase(c)) {
                    sb.setCharAt(i, Character.toLowerCase(c));
                } else if (Character.isLowerCase(c)) {
                    sb.setCharAt(i, Character.toUpperCase(c));
                }
            }
        } else {
            sb.reverse();
        }
        return sb.toString();
    }
}

