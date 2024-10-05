    int max_prime = 2;
    for(int i = 2; i < lst.size(); i++){
        if(isPrime(lst[i])){
            max_prime = lst[i];
        }
    }
    int sum = 0;
    while(max_prime > 0){
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}
bool isPrime(int n){
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i*i <= n; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}