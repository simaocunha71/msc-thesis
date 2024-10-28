    int max_prime = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (is_prime(lst[i]) && lst[i] > max_prime) {
            max_prime = lst[i];
        }
    }
    int sum = 0;
    while (max_prime > 0) {
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}

bool is_prime(int number) {
    if (number <= 1) {
        return false;
    }
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

