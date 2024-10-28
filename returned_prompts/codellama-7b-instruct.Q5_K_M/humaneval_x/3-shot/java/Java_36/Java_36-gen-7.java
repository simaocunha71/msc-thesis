        int count = 0;
        for (int i = 10; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String s = String.valueOf(i);
                for (int j = 0; j < s.length(); j++) {
                    if (s.charAt(j) == '7') {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}

