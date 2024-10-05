        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ((c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u') || (i == s.length() - 1 && c == 'y')) {
                count++;
            }
        }
        return count;
    }
}
