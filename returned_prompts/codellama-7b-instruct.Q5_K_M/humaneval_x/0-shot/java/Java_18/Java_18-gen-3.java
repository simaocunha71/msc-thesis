        int count = 0;
        int i = 0;
        while (i < string.length()) {
            int j = 0;
            while (j < substring.length()) {
                if (i + j >= string.length() || string.charAt(i + j) != substring.charAt(j)) {
                    break A;
                }
                j++;
            }
            count++;
            i = i + j;
        }
        return count;
    }
}