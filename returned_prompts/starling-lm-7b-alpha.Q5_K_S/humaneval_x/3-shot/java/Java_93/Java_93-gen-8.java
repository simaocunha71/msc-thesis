        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c == ' ') {
                result.append(c);
            } else if (c >= 'a' && c <= 'z') {
                int new_code = (c - 'a' + 1) % 26 + 'a';
                if (new_code == 'z') {
                    new_code = 'a';
                }
                result.append((char)new_code);
            } else if (c >= 'A' && c <= 'Z') {
                int new_code = (c - 'A' + 1) % 26 + 'A';
                if (new_code == 'Z') {
                    new_code = 'A';
                }
                result.append((char)new_code);
            }
        }
        return result.toString();
    }
}

