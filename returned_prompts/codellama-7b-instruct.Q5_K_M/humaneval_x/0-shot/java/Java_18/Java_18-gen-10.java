        int n = string.length();
        int m = substring.length();
        if (n < m) return 0;
        int count = 0;
        for (int i = 0; i < n - m + 1; i++) {
            if (string.substring(i, i + m).equals(substring)) {
                count++;
            }
        }
        return count;
    }
}
