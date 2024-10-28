        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                char ch = s.charAt(i);
                if (Character.isUpperCase(ch)) {
                    ch = Character.toLowerCase(ch);
                } else {
                    ch = Character.toUpperCase(ch);
                }
                s = s.substring(0, i) + ch + s.substring(i + 1);
                continue A;
            }
        }
        if (s.length() == 0) {
            s = new StringBuilder(s).reverse().toString();
        }
        return s;
    }
}