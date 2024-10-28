        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i % 2 == 0) {
                if (c == 'A' || c == 'E' || c == 'O' || c == 'U' || c == 'Y') {
                    count += 1;
                }
            }
        }
        return count;
    }
}

