    int i;
    int max_prime_factor = 1;
    for(i = 2; i <= n; i++) {
        if(n % i == 0) {
            int j;
            for(j = 2; j <= i / 2; j++) {
                if(i % j == 0) break;
            }
            if(j > i / 2) {
                if(i > max_prime_factor) {
                    max_prime_factor = i;
                }
            }
        }
    }
    return max_prime_factor;
}

B:
    int largest_prime_factor(int n) {
        int max_prime_factor = 1;
        for(int i = 2; i <= n; i++) {
            if(n % i == 0) {
                int is_prime = 1;
                for(int j = 2; j * j <= i; j++) {
                    if(i % j == 0) {
                        is_prime = 0;
                        break;
                    }
                }
                if(is_prime) {
                    if(i > max_prime_factor) {
                        max_prime_factor = i;
                    }
                }
            }
        }
        return max_prime_factor;
    }

C:
    int largest_prime_factor(int n) {
        int max_prime_factor = 1;
        for(int i = 2; i * i <= n; i++) {
            if(n % i == 0) {
                int j;
                for(j = i; j * j <= n; j += i) {
                    n /= j;
                }
                if(n > 1) {
                    max_prime_factor = n;
                } else {
                    max_prime_factor = i;
                }
            }
        }
        return max_prime_factor;
    }

D:
    int largest_prime_factor(int n) {
        int max_prime_factor = 1;
        for(int i = 2; i * i <= n; i++) {
            if(n % i == 0) {
                int is_prime = 1;
                for(int j = 2; j * j <= i; j++) {
                    if(i % j == 0) {
                        is_prime = 0;
                        break;
                    }
                }
                if(is_prime) {
                    if(i > max_prime_factor) {
                        max_prime_factor = i;
                    }
                }
                while(n % i == 0) {
                    n /= i;
                }
            }
        }
        if(n > 1) {
            max