        int result = 1;
        int sign = n < 0 ? -1 : 1;
        n = Math.abs(n);

        while (n > 0) {
            int d = n % 10;
            if (d % 2 != 0) result *= d;
            n /= 10;
        }
        return result * sign;
    }
}

