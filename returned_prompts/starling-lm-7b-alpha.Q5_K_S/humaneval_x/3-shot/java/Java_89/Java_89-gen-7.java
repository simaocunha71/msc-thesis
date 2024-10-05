        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c += 2;
                if (c > 'z') {
                    c -= 26;
                }
            } else if (c >= 'A' && c <= 'Z') {
                c += 2;
                if (c > 'Z') {
                    c -= 26;
                }
            }
            result.append(c);
        }
        return result.toString();
    }
}

