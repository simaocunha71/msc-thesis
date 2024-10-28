        int fibonacci = 0;
        int previous = 1;
        int current = 1;
        int result = 0;
        int count = 0;

        while (count < n) {
            fibonacci = previous + current;
            previous = current;
            current = fibonacci;

            if (fibonacci > 1) {
                if (isPrime(fibonacci)) {
                    result = fibonacci;
                    count++;
                }
            }
        }
        return result;
    }

    private boolean isPrime(int number) {
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}


public class CodeChallenges {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.primeFib(10));
    }
}

```