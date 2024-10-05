        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(factorial(i));
            } else {
                result.add(sum_to_n(i));
            }
        }
        return result;
    }

    /**
    Recursive function to calculate factorial
    >>> factorial(5)
    120
     */
    public int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    /**
    Calculate the sum of numbers from 1 to n
    >>> sum_to_n(5)
    15
     */
    public int sum_to_n(int n) {
        if (n == 0) {
            return 0;
        } else {
            return n + sum_to_n(n - 1);
        }
    }
}


public class Main {
    public static void main(String[] args) {
        // Use Solution class to perform tests
        Solution solution = new Solution();

        // Test hasCloseElements
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));

        // Test separateParenGroups
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));

        // Test truncateNumber
        System.out.println(solution.truncateNumber(3.5));

        // Test f
        System.out.println(solution.f(5));
    }
}
```