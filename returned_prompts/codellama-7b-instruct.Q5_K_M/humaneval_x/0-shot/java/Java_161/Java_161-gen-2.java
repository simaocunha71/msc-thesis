        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                if (Character.isLowerCase(s.charAt(i))) {
                    s = s.substring(0, i) + Character.toUpperCase(s.charAt(i)) + s.substring(i + 1);
                } else {
                    s = s.substring(0, i) + Character.toLowerCase(s.charAt(i)) + s.substring(i + 1);
                }
                continue A;
            }
        }
        return s;
    }
}

