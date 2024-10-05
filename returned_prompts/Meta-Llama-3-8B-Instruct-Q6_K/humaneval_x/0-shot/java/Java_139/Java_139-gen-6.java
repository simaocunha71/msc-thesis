        if(n <= 0){
            return 0;
        }
        long result = 1;
        for(int i = 1; i <= n; i++){
            result *= factorial(i);
        }
        return result;
    }

    private long factorial(int n){
        long result = 1;
        for(int i = 2; i <= n; i++){
            result *= i;
        }
        return result;
    }
}
// The specialFactorial function calculates the Brazilian factorial of a given integer n.
// It does this by calling the factorial function, which calculates the factorial of a given integer.
// The specialFactorial function multiplies all these factorials together to get the Brazilian factorial.
// If n is less than or equal to 0, the function returns 0, as the Brazilian factorial is not defined for non-positive integers.