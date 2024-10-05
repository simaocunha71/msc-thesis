        String result = "";
        while (N != 0) {
            int mod = N % 2;
            result = mod + result;
            N = N / 2;
        }
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.truncateNumber(1000));
        System.out.println(solution.truncateNumber(150));
        System.out.println(solution.solve(1000));
        System.out.println(solution.solve(150));
        System.out.println(solution.solve(147));
    }
}
```