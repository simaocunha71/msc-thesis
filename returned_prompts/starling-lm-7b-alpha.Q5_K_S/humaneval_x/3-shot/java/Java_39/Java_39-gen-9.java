        int fib = 0;
        int last_fib = 1;
        int next_fib = 1;

        for (int i = 0; i < n; i++) {
            fib = next_fib;
            next_fib = fib + last_fib;
            last_fib = fib;
            if (isPrime(fib)) return fib;
        }
        return -1;
    }

    public boolean isPrime(int number) {
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}


class ProblemSolver {

    public static void main(String[] args) {
        Solution solution = new Solution();

        solution.separateParenGroups("( ) (( )) (( )( ))"); // ["()", "(())", "(()())"]
        solution.truncateNumber(3.5); // 0.5
        solution.primeFib(5); // 89
    }
}
```