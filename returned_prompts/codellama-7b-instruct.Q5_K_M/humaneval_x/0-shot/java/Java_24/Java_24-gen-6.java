    if (n == 0) {
        return 0;
    }
    for (int i = n / 2; i > 0; i--) {
        if (n % i == 0) {
            return i;
        }
    }
    return 0;
}

/**
For a given number n, find the smallest number that divides n evenly, larger than n
>>> smallestDivisor(15)
30
*/
public int smallestDivisor(int n) {
    if (n == 0) {
        return 0;
    }
    for (int i = n * 2; i > n; i--) {
        if (i % n == 0) {
            return i;
        }
    }
    return 0;
}
}







