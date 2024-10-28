        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= factorial(i);
        }
        return result;
    }

    public long factorial(int n) {
        if (n == 0 || n == 1) return 1;
        return n * factorial(n - 1);
    }
}

