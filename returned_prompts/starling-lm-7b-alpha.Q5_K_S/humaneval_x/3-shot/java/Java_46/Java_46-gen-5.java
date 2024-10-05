        if (n <= 0) return 0;

        if (n == 1) return 0;
        if (n == 2) return 2;
        if (n == 3) return 0;

        int fib_n = 0;
        int fib_n_minus_1 = 0;
        int fib_n_minus_2 = 2;
        int fib_n_minus_3 = 0;

        for (int i = 0; i < n; i++) {
            int temp = fib_n;
            fib_n = fib_n_minus_1;
            fib_n_minus_1 = fib_n_minus_2;
            fib_n_minus_2 = fib_n_minus_3;
            fib_n_minus_3 = temp;
        }
        return fib_n;
    }
}



public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.fib4(5));
        System.out.println(solution.fib4(6));
        System.out.println(solution.fib4(7));
    }
}
```