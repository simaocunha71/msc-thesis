        int count = 0;
        for (int i = 0; i < string.length(); i++) {
            if (string.substring(i).startsWith(substring)) count++;
        }
        return count;
    }
}

