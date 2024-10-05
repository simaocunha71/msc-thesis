    int start1 = max(interval1[0], interval2[0]);
    int end1 = min(interval1[1], interval2[1]);
    if (start1 > end1) {
        return "NO";
    }
    int length = end1 - start1 + 1;
    if (isPrime(length)) {
        return "YES";
    }
    return "NO";
}

bool isPrime(int number) {
    if (number <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(number); i++) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}