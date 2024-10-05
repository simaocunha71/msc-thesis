    int max_prime = 0;
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (isPrime(lst[i])) {
            if (lst[i] > max_prime) {
                max_prime = lst[i];
            }
        }
    }
    while (max_prime > 0) {
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}  // Function to check if a number is prime


