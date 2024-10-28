        int count = 0;
        for (int i = 11; i < n; i += 11) {
            if (i % 13 == 0 || i % 11 == 0) {
                String s = Integer.toString(i);
                for (char c : s.toCharArray()) {
                    if (c == '7') count += 1;
                }
            }
        }
        return count;
    }
}

