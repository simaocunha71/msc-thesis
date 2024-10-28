        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String i_str = Integer.toString(i);
                for (char c : i_str.toCharArray()) {
                    if (c == '7') count += 1;
                }
            }
        }
        return count;

    }
}

