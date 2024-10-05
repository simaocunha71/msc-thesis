    for(int i=2; i <= sqrt(n); i++){
        if(n % i == 0){
            n = n / i;
            i--;
        }
    }
    return n;
}


