        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            result.add(i % 2 == 0 ? factorial(i) : sum(i));
        }
        return result;
    }

    private int factorial(int n) {
        if (n == 1) return 1;
        return n * factorial(n - 1);
    }

    private int sum(int n) {
        return (n * (n + 1)) / 2;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.f(5));
    }
}
```