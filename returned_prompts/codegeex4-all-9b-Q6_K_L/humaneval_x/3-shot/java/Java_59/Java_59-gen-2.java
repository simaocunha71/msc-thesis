        int largest_prime = 2;
        while (n % 2 == 0) {
            n /= 2;
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest_prime = i;
                n /= i;
            }
        }

        if (n > 2) largest_prime = n;
        return largest_prime;
    }
}

