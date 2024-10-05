        for (int i = 2; i <= n / i; i++) {
            while (n % i == 0) {
                n /= i;
            }
            if (n == 1) return i;
        }
        return n;

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.largestPrimeFactor(13195));
        System.out.println(s.largestPrimeFactor(2048));
    }
}

