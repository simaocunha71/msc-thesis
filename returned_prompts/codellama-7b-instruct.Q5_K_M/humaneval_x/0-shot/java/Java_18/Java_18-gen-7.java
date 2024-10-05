        int count = 0;
        if (string.length() == 0) return 0;
        if (substring.length() == 0) return 1;
        if (string.length() < substring.length()) return 0;
        if (string.length() == substring.length()) return string.equals(substring) ? 1 : 0;
        for (int i = 0; i <= string.length() - substring.length(); i++) {
            if (string.substring(i, i + substring.length()).equals(substring)) count++;
        }
        return count;
    }
}
