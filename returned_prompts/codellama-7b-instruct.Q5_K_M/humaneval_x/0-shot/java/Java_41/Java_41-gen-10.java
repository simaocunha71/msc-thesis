        int n = 1000000000;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                for (int j = i + 1; j < n; j++) {
                    if (j % 2 == 1) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}




