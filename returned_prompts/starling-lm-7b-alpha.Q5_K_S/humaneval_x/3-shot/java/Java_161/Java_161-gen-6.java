        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                sb.append(Character.isLowerCase(s.charAt(i)) ? Character.toUpperCase(s.charAt(i)) : Character.toLowerCase(s.charAt(i)));
            } else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}

