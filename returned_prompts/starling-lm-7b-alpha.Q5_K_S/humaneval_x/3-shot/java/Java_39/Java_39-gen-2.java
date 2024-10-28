        int fib = 0;
        int fib_n = 1;
        int fib_n_1 = 1;
        int current = 2;

        while (current < n) {
            fib = fib_n_1;
            fib_n_1 = fib_n + fib;
            fib_n = fib;
            current = fib_n_1;

            if (current % 2 == 0) continue;

            boolean isPrime = true;
            for (int i = 3; i * i <= current; i += 2) {
                if (current % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) return current;
        }
        return -1;
    }
}


public class ProblemSolutions {
    public static void main(String[] args) {
        Solution sol = new Solution();
        sol.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3);
        sol.separateParenGroups("( ) (( )) (( )( ))");
        System.out.println(sol.truncateNumber(3.5));
        System.out.println(sol.primeFib(1));
        System.out.println(sol.primeFib(2));
        System.out.println(sol.primeFib(3));
        System.out.println(sol.primeFib(4));
        System.out.println(sol.primeFib(5));
    }
}

```