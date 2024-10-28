        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isPrime(6)); // false
        System.out.println(solution.isPrime(101)); // true
        System.out.println(solution.isPrime(11)); // true
        System.out.println(solution.isPrime(13441)); // true
        System.out.println(solution.isPrime(61)); // true
        System.out.println(solution.isPrime(4)); // false
        System.out.println(solution.isPrime(1)); // false
    }
}

