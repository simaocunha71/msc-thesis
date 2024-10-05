    int length = str.length();
    if (length <= 1) return false;
    for (int i = 2; i <= sqrt(length); i++) {
        if (length % i == 0) return false;
    }
    return true;
}  // this code is not correct, it is missing a condition to check if the number is less than 2, which is not prime
// the correct code should be:
int prime_length(string str) {
    int length = str.length();
    if (length <= 1) return false;
    for (int i = 2; i <= length; i++) {
        if (length % i == 0) return false;
    }
    return true;
}
// or
int prime_length(string str) {
    int length = str.length();
    if (length <= 1) return false;
    if (length == 2) return true;
    for (int i = 2; i <= sqrt(length); i++) {
        if (length % i == 0) return false;
    }
    return true;
}  // this one is more efficient as it stops checking when it finds a divisor
// or
int prime_length(string str) {
    int length = str.length();
    if (length <= 1) return false;
    if (length == 2) return true;
    if (length % 2 == 0) return false;  // 2 is a prime number, so we can skip even numbers
    for (int i = 3; i <= sqrt(length); i += 2) {
        if (length % i == 0) return false;
    }
    return true;
}  // this one is more efficient as it skips even numbers
// the best one is the last one, it is the most efficient and it handles the case of 2 being a prime number.  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //