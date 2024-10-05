        if (a == 1) return false;

        int b = 2;
        while (a % b == 0) {
            a /= b;
            if (!isPrime(b)) return false;
            if (a == 1) return true;
        }
        return false;
    }

    public boolean isPrime(int b) {
        for (int i = 2; i * i <= b; i++) {
            if (b % i == 0) return false;
        }
        return true;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.separateParenGroups("( () (()) (()()) ()() (()()) () () "));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.isMultiplyPrime(30));
    }
}
```