        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append((char)(c - 'a' + 'A'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char)(c + 'a' - 'A'));
            } else {
                result.append(c);
            }
        }
        StringBuilder result2 = new StringBuilder();
        for (char c : result.toString().toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result2.append((char)(c + 2));
                if (result2.charAt(result2.length() - 1) > 'z')
                    result2.setLength(result2.length() - 1);
            } else {
                result2.append(c);
            }
        }
        return result2.toString();
    }
}

