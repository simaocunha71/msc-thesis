        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i % 2 == 0 && c >= 'A' && c <= 'Z' && (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')) {
                count += 1;
            }
        }
        return count;
    }
}

