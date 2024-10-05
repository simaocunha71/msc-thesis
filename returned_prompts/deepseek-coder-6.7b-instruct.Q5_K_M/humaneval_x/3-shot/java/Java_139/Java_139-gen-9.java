        long result = 1;
        for(int i = n; i > 0; i--){
            result *= factorial(i);
        }
        return result;
    }

    public long factorial(int n) {
        long result = 1;
        for(int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}

