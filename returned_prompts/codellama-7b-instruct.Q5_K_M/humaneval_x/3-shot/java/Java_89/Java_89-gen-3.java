        String result = "";
        for (char c : s.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                if (Character.isLowerCase(c)) {
                    result += (char) ((c - 'a' + 2 * 2) % 26 + 'a');
                } else {
                    result += (char) ((c - 'A' + 2 * 2) % 26 + 'A');
                }
            } else {
                result += c;
            }
        }
        return result;
    }
}

