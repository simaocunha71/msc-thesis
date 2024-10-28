    long result = 1;
    for(int i = 1; i <= n; i++) {
        result *= factorial(i);
    }
    return result;
}

private long factorial(int n) {
    long result = 1;
    for(int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

B:
    public long specialFactorial(int n) {
        long result = 1;
        for(int i = 1; i <= n; i++) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        long result = 1;
        for(int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

C:
    public long specialFactorial(int n) {
        long result = 1;
        for(int i = n; i >= 1; i--) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        long result = 1;
        for(int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

D:
    public long specialFactorial(int n) {
        if(n <= 0) {
            return 0;
        }
        long result = 1;
        for(int i = 1; i <= n; i++) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        if(n <= 1) {
            return 1;
        }
        long result = 1;
        for(int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }E:
    public long specialFactorial(int n) {
        if(n <= 0) {
            return 0;
        }
        long result = 1;
        for(int i = 1; i <= n; i++) {
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n) {
        if(n <= 1) {
            return 1;
        }
        long result = 1;
        for(int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
F:
    public long specialFactorial(int n) {
