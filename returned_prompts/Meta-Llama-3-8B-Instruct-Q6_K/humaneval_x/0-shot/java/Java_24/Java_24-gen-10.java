        int largestDivisor = 0;
        for(int i = 1; i < n; i++) {
            if(n % i == 0) {
                largestDivisor = i;
            }
        }
        return largestDivisor;
    }
}

