        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String s = String.valueOf(i);
                for (char c : s.toCharArray()) {
                    if (c == '7') {
                        count += 1;
                    }
                }
            }
        }
        return count;
    }
}

