    int max_prime = 2;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] > max_prime) {
            int sum = 0;
            for (int j = lst[i]; j > 0; j /= 10) {
                sum += j % 10;
            }
            max_prime = lst[i];
        }
        for (int j = 2; j * j <= lst[i]; j++) {
            if (lst[i] % j == 0) {
                break;
            }
        }
        if (j * j > lst[i]) {
            int sum = 0;
            for (int j = lst[i]; j > 0; j /= 10) {
                sum += j % 10;
            }
            if (sum > 0 && sum > max_prime) {
                max_prime = sum;
            }
        }
    }
    return max_prime;
}
// This function is not working correctly, it seems to be returning the smallest prime number in the list instead of the largest prime number and the sum of its digits. It also doesn't handle non-prime numbers correctly. 

