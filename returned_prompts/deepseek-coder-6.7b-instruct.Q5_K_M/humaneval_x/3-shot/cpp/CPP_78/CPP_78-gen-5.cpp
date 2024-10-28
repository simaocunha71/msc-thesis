    int primeCount = 0;
    int len = num.length();
    for(int i = 0; i < len; i++){
        if(num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7' || num[i] == 'B' || num[i] == 'D'){
            primeCount++;
        }
    }
    return primeCount;
}

