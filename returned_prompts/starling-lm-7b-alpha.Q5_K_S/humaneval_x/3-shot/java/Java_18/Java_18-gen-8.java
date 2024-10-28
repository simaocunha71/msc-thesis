        int count = 0;
        for (int i = 0; i < string.length(); i++) {
            int j = i;
            while (j < string.length() && string.charAt(j) == substring.charAt(0)) {
                if (string.substring(i, i + substring.length()).equals(substring)) {
                    count += 1;
                }
                j += 1;
            }
        }
        return count;
    }
}

