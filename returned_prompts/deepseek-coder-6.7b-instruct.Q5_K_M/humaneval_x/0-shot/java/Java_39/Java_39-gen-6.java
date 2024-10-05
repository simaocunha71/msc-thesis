        ArrayList<Integer> primes = new ArrayList<>();
        ArrayList<Integer> fibs = new ArrayList<>();
        int fib1 = 1, fib2 = 1, fib3;
        int prime = 2;

        while (primes.size() < n || fibs.size() < n) {
            if (isPrime(prime)) {
                primes.add(prime);
            }
            if (isFib(fib2)) {
                fibs.add(fib2);
            }
            fib3 = fib1 + fib2;
            fib1 = fib2;
            fib2 = fib3;
            prime++;
        }

        if (primes.size() >= n) {
            return primes.get(n - 1);
        } else {
            return fibs.get(n - 1);
        }
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    private boolean isFib(int num) {
        int a = 0, b = 1;
        while (b < num) {
            int temp = b;
            b = a + b;
            a = temp;
        }
        return b == num;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.primeFib(1));  // 2
        System.out.println(solution.primeFib(2));  // 3
        System.out.println(solution.primeFib(3));  // 5
        System.out.println(solution.primeFib(4));  // 13
        System.out.println(solution.primeFib(5));  // 89
    }
}

Here, we are using two lists: primes and fibs to keep track