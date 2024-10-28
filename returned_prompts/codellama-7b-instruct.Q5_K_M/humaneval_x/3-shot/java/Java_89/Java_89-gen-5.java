        String result = "";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    c = (char) (c + 2 * 2);
                } else if (Character.isUpperCase(c)) {
                    c = (char) (c + 2 * 2 - 'A' + 'a');
                }
            }
            result += c;
        }
        return result;
    }
}

