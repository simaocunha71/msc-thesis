        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                while (n % i == 0) {
                    n /= i;
                }
                if (isPrime(i)) {
                    return i;
                }
            }
        }
        return -1;
    }

    public boolean isPrime(int i) {
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                return false;
            }
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.largestPrimeFactor(13195));
        System.out.println(s.largestPrimeFactor(2048));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
    }
}
```