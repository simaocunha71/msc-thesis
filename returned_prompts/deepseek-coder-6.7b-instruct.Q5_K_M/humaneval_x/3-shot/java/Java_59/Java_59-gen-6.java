        int largest_prime = -1;
        for  (int i = 2; i <= n; i++) {
            while  (n % i == 0) {
                largest_prime = i;
                n /= i;
            }
        }
        return largest_prime;
     }
}

