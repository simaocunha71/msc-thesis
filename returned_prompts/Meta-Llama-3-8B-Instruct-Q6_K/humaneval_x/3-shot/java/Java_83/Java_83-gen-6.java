        int count = 0;
        for (int i = 10; i < Math.pow(10, n); i++) {
            if (i % 10 == 1 || i / (int) Math.pow(10, n - 1) % 10 == 1) {
                count++;
            }
        }
        return count;
    }
}

