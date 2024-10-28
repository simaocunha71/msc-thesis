    int count = 0;
    for (int i = 0; i < num.length(); i++) {
        char c = toupper(num[i]);
        if (c >= '2' && c <= '9') {
            if (isPrime(atoi(&c))) {
                count++;
            }
        } else if (c == 'B' || c == 'D' || c == 'F') {
            count++;
        }
    }
    return count;
}

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}