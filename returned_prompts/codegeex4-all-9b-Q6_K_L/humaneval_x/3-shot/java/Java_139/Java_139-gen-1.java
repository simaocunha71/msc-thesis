        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        if (n == 1) return 1;
        return n * factorial(n - 1);
    }
}

