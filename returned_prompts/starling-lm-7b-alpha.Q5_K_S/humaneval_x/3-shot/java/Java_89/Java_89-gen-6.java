        char[] chars = s.toCharArray();
        for (char c : chars) {
            if (c >= 'a' && c <= 'z') {
                c = (char)((c - 'a' + 2 * 2) % 26 + 'a');
            } else if (c >= 'A' && c <= 'Z') {
                c = (char)((c - 'A' + 2 * 2) % 26 + 'A');
            }
        }
        return new String(chars);
    }
}

