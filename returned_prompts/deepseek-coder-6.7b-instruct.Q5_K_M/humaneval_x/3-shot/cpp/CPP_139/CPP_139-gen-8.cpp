    long long result = 1;
    for(int i = n; i > 0; i--){
        long long fact = 1;
        for(int j = 1; j <= i; j++){
            fact *= j;
        }
        result *= fact;
    }
    return result;
}

