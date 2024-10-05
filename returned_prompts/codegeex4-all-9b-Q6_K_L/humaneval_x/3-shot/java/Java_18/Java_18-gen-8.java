        int count = 0;
        for (int i = 0; i < string.length(); i++) {
            if (string.startsWith(substring, i)) count += 1;
        }
        return count;
    }
}

