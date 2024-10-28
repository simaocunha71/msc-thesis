    int largest = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            if (i > largest) {
                largest = i;
            }
        }
    }
    if (n > largest) {
        largest = n;
    }
    return largest;
}