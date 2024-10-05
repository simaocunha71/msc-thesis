        int count = 0;
        for (int i = 1; i < 10; i++) {
            count += 1;
        }
        for (int i = 1; i < 10; i++) {
            count += Math.pow(10, n - 1) * 9;
        }
        return count;
    }
}

