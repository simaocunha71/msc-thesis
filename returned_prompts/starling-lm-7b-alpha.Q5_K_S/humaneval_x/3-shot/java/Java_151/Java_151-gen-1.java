        int result = 0;
        for (Object number : lst) {
            if (number instanceof Integer) {
                int n = (Integer)number;
                if (n >= 0 && n % 2 == 1) {
                    result += n * n;
                }
            }
        }
        return result;
    }
}






public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));

        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.separateParenGroups("( )( ()( )( ()(( )( ()( (()())))()"));

        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.truncateNumber(3.6));
        System.out.println(solution.truncateNumber(3.0));

        System.out.println(solution.doubleTheDifference(Arrays.asList(1, 3, 2, 0)));
        System.out.println(solution.doubleTheDifference(Arrays.asList(-1, -2, 0)));
        System.out.println(solution.doubleTheDifference(Arrays.asList(9, -2)));
        System.out.println(solution.doubleTheDifference(Arrays.asList(0)));
    }
}

```