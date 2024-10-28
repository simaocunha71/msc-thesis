        int largest = 2;

        while (n % 2 == 0) {
            n /= 2;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n /= i;
            }
        }
        if (n > 2) {
            largest = n;
        }
        return largest;
    }
}

