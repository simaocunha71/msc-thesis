        int total_hex_digits = hexKey(hex_number);
        int primes_count = 0;
        for (int i = 0; i < total_hex_digits; i++) {
            int digit = hex_number.charAt(i);
            if (isPrime(digit) == 1) {
                primes_count += 1;
            }
        }
        return primes_count;
    }
}

