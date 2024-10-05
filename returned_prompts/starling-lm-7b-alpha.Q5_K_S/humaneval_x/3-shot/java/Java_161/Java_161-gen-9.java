        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                result.append(Character.isLowerCase(c) ? (char)(c - 'a' + 'A') : (char)(c - 'A' + 'a'));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

