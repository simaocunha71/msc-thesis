        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                c = Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c);
            } else {
                // if it's not a letter, keep it as it is
            }
            sb.append(c);
        }
        return sb.toString();
    }
}
