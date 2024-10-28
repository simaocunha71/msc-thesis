        int result = 0;
        for (Integer i : lst) {
            if (isPrime(i)) {
                result += getSumOfDigits(i);
            }
        }
        return result;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;

        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i = i + 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }

        return true;
    }

    public int getSumOfDigits(int number) {
        String str = String.valueOf(number);
        int result = 0;
        for (char c : str.toCharArray()) {
            result += Character.getNumericValue(c);
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.skjkasdkd(Arrays.asList(0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3)));
    }
}
```