        if (n == 1 || n == 0) return y;
        for (int i = 2; i < n / 2; i++) {
            if (n % i == 0) return y;
        }
        return x;
     }
}

