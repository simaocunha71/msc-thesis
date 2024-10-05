        StringBuilder sb = new StringBuilder();
        boolean hasLetter = false;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                sb.append(Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
                hasLetter = true;
            } else {
                sb.append(c);
            }
        }
        if (!hasLetter) {
            return sb.reverse().toString();
        }
        return sb.toString();
    }
}

