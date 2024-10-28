        int count = 0;
        for (int i = 0; i < string.length() - substring.length() + 1; i++) {
            if (string.substring(i, i + substring.length()).equals(substring)) count++;
        }
        return count;
    }
}

