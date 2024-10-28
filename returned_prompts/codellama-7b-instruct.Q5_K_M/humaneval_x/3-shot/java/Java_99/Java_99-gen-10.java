        int count = 0;
        for (char c : value.toCharArray()) {
            if (c == 'A' || c == 'a') count += 1;
        }
        return count;
    }
}

