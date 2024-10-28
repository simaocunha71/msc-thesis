        int count = 0;
        for (int i = 0; i < string.length(); i++) {
            int j = i;
            while (j < string.length() && substring.charAt(0) == string.charAt(j)) {
                if (substring.equals(string.substring(j, j + substring.length()))) {
                    count += 1;
                }
                j += 1;
            }
        }
        return count;
    }
}

