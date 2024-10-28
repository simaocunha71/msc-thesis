        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                int c_i = c - 'a';
                c = (char) (((c_i + 1) % 26) + 'a');
            } else if (c >= 'A' && c <= 'Z') {
                int c_i = c - 'A';
                c = (char) (((c_i + 1) % 26) + 'A');
            }
            result.append(c);
        }
        return result.toString();
    }
}

