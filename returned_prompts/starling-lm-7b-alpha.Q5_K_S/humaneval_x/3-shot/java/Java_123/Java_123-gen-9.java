        List<Integer> result = new ArrayList<>();
        result.add(n);

        while (n != 1) {
            if (n % 2 == 1) {
                result.add(n);
                n = 3 * n + 1;
            } else {
                result.add(n);
                n /= 2;
            }
        }
        Collections.sort(result);
        return result;
    }
}



public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(Arrays.toString(solution.getOddCollatz(5)));
    }
}
```