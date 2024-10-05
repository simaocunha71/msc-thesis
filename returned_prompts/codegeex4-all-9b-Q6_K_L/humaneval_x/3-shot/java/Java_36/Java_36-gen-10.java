        int count = 0;
        for (int i = 0; i < n; i++) {
            if ((i % 11 == 0 || i % 13 == 0) && Integer.toString(i).contains("7")) {
                count += 1;
            }
        }
        return count;
    }
}

