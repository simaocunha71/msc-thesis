        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append((char) (c - 'a' + 'A'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char) (c - 'A' + 'a'));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

