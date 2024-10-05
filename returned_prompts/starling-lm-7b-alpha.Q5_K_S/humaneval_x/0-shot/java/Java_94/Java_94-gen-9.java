        int max = 0;
        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                int temp = lst.get(i);
                while (temp != 0) {
                    sum += temp % 10;
                    temp /= 10;
                }
                if (sum > max) {
                    max = sum;
                }
                sum = 0;
            }
        }
        return max;
    }

    private static boolean isPrime(int n) {
        if (n == 2) {
            return true;
        }
        if (n < 2 || (n % 2 == 0 && n != 2)) {
            return false;
        }
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

























































































































































































































































