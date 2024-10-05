        int result = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String s = Integer.toString(i);
                if (s.contains("7")) {
                    result += 1;
                }
            }
        }
        return result;
    }
}

