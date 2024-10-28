        int counter = 0;
        for (int i = 0; i <= string.length() - substring.length(); i++) {
            if (string.substring(i, i + substring.length()).equals(substring)) {
                counter += 1;
            }
        }
        return counter;
    }
}

