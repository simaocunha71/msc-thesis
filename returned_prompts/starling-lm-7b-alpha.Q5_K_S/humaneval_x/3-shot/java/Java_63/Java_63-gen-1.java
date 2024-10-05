        int[] result = new int[n + 1];
        result[0] = 0;
        result[1] = 0;
        result[2] = 1;

        for (int i = 3; i <= n; i++) {
            result[i] = result[i - 1] + result[i - 2] + result[i - 3];
        }
        return result[n];
    }
}

public class CodeChallenges {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.fibfib(1));
        System.out.println(s.fibfib(5));
        System.out.println(s.fibfib(8));
    }
}

```