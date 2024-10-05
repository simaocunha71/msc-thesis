        if (n == 0) {
            return 1;
        }
        if (n % 2 == 1) {
            return (int)((long)pow2(n - 1) * (long)2 % (int)Math.pow(2, 31));
        } else {
            int m = pow2(n / 2);
            return (int)((long)m * m % (int)Math.pow(2, 31));
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.modp(3, 5));
        System.out.println(sol.pow2(3));
        System.out.println(sol.pow2(1101));
        System.out.println(sol.pow2(0));
        System.out.println(sol.pow2(100));
    }
}

































































































