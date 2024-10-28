        int a = 0;
        int b = 1;
        int c = 1;

        while (n > 0) {
            int temp = a;
            a = b;
            b = c;
            c = temp + b;
            if (c > n) return c;
            if (is_prime(c)) return c;
        }
        return c;
    }

    boolean is_prime(int x) {
        if (x == 2) return true;
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
}


