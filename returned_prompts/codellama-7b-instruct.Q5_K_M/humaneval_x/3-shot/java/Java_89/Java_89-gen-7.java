        String result = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    int offset = 'A' - 2 * 2;
                    result += (char) (((c - offset + 26) % 26) + offset);
                } else {
                    int offset = 'a' - 2 * 2;
                    result += (char) (((c - offset + 26) % 26) + offset);
                }
            } else {
                result += c;
            }
        }
        return result;
    }
}

