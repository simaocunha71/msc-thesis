        if (n <= 3) return 0;
        if (n == 4) return 2;

        int fib4_n_minus_1 = 0;
        int fib4_n_minus_2 = 0;
        int fib4_n_minus_3 = 0;
        int fib4_n_minus_4 = 0;
        int fib4_n = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                fib4_n_minus_4 = 0;
            } else if (i == 1) {
                fib4_n_minus_3 = 0;
            } else if (i == 2) {
                fib4_n_minus_2 = 0;
            } else if (i == 3) {
                fib4_n_minus_1 = 0;
            }
            if (i > 3) {
                fib4_n = fib4_n_minus_1 + fib4_n_minus_2 + fib4_n_minus_3 + fib4_n_minus_4;
            }
        }
        return fib4_n;
    }
}

public class ProblemSolutions {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.fib4(5));
        System.out.println(s.fib4(6));
        System.out.println(s.fib4(7));
    }
