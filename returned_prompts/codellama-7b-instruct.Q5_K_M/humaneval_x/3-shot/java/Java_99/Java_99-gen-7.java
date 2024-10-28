        int count = 0;
        for (char c : value.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                count += 1;
            }
        }
        return count;
    }
}

