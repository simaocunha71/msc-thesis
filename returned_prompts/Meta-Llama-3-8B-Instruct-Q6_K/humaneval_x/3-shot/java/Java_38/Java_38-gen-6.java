        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i += 3) {
            if (i + 1 < s.length()) {
                result.append(s.charAt(i + 1));
            }
            result.append(s.charAt(i));
            if (i + 2 < s.length()) {
                result.append(s.charAt(i + 2));
            }
        }
        return result.toString();
    }
}

