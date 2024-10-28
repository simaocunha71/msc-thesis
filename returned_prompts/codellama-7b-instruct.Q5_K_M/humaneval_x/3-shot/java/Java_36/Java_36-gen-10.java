        int count = 0;
        for (int i = 10; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String num_str = String.valueOf(i);
                for (char c : num_str.toCharArray()) {
                    if (c == '7') count++;
                }
            }
        }
        return count;
    }
}

