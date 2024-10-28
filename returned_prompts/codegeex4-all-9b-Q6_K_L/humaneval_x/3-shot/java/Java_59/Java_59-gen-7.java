        int largest = 0;
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }
        return largest;
    }
}

