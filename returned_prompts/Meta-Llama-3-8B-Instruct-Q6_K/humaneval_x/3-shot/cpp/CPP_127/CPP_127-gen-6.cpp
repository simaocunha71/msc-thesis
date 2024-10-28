    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if (start > end)
        return "NO";
    int length = end - start + 1;
    if (length < 2)
        return "NO";
    for (int i = 2; i <= sqrt(length); i++) {
        if (length % i == 0)
            return "NO";
    }
    return "YES";
}
// Function to check if a number is prime
bool isPrime(int num) {
    if (num <= 1)
        return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}
// Function to check if a number is prime
bool isPrime(int num) {
    if (num <= 1)
        return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}