public int largestPrimeFactor(int n) {
        int largest = 2;
        while (n > largest * largest) {
            if (n % largest == 0) {
                n /= largest;
            } else {
                largest++;
            }
        }
        return n;
    }