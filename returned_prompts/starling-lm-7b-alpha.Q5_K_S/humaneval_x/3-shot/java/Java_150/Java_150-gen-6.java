        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return y;
        }
        return x;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        // solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5);
        // solution.separateParenGroups("( ) (( )) (( )( ))");
        // solution.truncateNumber(3.5);
        // solution.xOrY(7, 34, 12);
        // solution.xOrY(15, 8, 5);
    }
}
```