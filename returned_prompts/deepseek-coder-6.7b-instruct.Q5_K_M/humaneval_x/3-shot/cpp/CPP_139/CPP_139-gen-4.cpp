    long long result = 1;
    for(int i = n; i > 0; i--) {
        long long temp = 1;
        for(int j = i; j > 0; j--) {
            temp *= j;
        }
        result *= temp;
    }
    return result;
}



