        long result = 1;
        for (int i = n; i > 0; i--) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        long result = 1;
        for (int i = n; i > 0; i--) {
            result *= i;
        }
        return result;
    }
}

