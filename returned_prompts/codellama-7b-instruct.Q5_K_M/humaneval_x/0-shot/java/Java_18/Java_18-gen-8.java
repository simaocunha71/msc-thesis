        if (string.length() == 0 || substring.length() == 0) return 0;

        int count = 0;
        int start = 0;

        while (start <= string.length() - substring.length()) {
            if (string.substring(start, start + substring.length()).equals(substring)) count++;
            start++;
        }
        return count;
    }
}
