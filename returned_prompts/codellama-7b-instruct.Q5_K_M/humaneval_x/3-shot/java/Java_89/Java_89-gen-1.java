        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                int shift = (int)(c - 'a') * 2;
                shift = shift % 26;
                if (Character.isUpperCase(c)) {
                    result.append((char)(shift + 'A'));
                } else {
                    result.append((char)(shift + 'a'));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

