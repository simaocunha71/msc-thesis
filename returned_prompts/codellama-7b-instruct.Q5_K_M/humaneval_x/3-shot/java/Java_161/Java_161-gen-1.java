        char[] result = new char[s.length()];
        int index = 0;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                if (c >= 'a' && c <= 'z') {
                    result[index] = Character.toUpperCase(c);
                } else {
                    result[index] = Character.toLowerCase(c);
                }
            } else {
                result[index] = c;
            }
            index += 1;
        }
        return String.valueOf(result);
    }
}

