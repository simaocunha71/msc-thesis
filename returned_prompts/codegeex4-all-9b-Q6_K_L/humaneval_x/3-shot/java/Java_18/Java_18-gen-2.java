        int count = 0;
        int i = 0;
        while (i < string.length()) {
            if (string.substring(i).startsWith(substring)) {
                count += 1;
                i += substring.length();
            } else {
                i += 1;
            }
        }
        return count;
    }
}

