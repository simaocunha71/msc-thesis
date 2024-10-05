        int count = 0;
        for (char c : value.toCharArray()) {
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                count += 1;
            }
        }
        return count;
    }
}

