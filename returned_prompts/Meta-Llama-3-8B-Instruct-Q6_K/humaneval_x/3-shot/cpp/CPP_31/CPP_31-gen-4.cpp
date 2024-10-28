    if (n <= 1) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (long long i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
//Note: This function only checks for divisibility up to the square root of n
//This is because a larger factor of the number would be a multiple of smaller factor that has already been checked.
//This makes the function more efficient.