        int count = 0;
        int n = string.length();
        int m = substring.length();
        for (int i = 0; i < n - m + 1; i++) {
            if (string.substring(i, i + m).equals(substring)) {
                count++;
            }
        }
        return count;
    }
}
