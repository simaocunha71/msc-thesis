        int result = 0;
        for (int i = 1; i < Math.pow(10, n - 1); i++) {
            if ((i % 10 == 1) || (i / Math.pow(10, n - 1) == 1)) result += 1;
        }
        return result;
    }
}

