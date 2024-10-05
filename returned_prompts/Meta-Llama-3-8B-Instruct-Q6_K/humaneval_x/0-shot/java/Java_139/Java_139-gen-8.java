    public long specialFactorial(int n) {
        long result = 1;
        for(int i = 1; i <= n; i++){
            result *= factorial(i);
        }
        return result;
    }

    public long factorial(int n) {
        long result = 1;
        for(int i = 1; i <= n; i++){
            result *= i;
        }
        return result;
    }
}  // The above code is used to calculate the special factorial of a number. It takes an integer as input and returns the result.

