        List<Integer> result = new ArrayList<>();
        result.add(n);
        while (n != 1) {
            if (n % 2 == 1) {
                n = 3 * n + 1;
                result.add(n);
            } else {
                n /= 2;
                result.add(n);
            }
        }
        Collections.sort(result);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        // Test code here
        System.out.println(Solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(Solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(Solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(Solution.truncateNumber(3.5));
        System.out.println(Solution.getOddCollatz(5));
    }
}
```