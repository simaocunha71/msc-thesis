        while (true) {
            int i = 2;
            while (i * i <= n) {
                if (n % i == 0) {
                    n = n / i;
                    continue A;
                }
                i++;
            }
            return n;
        }
    }
}

