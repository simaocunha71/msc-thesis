    for(int i = 2; i <= n; i += 2) {
        int sum = 0;
        for(int j = 2; j <= n; j += 2) {
            if(i + j <= n) {
                sum += i + j;
                if(sum == n) {
                    return true;
                }
            }
        }
    }
    return false;
} // This is a brute force solution, can be optimized with better algorithm.


