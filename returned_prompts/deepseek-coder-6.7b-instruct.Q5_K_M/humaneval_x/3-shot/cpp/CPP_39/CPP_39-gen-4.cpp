    int a = 2;
    int b = 3;
    int c;
    int count = 2;
    if(n == 1) return a;
    if(n == 2) return b;
    while(count < n){
        c = a + b;
        a = b;
        b = c;
        if(is_prime(c)){
            count++;
        }
    }
    return c;
}
bool is_prime(int num){
    if(num <= 1) return false;
    if(num % 2 == 0 && num > 2) return false;
    for(int i = 3; i * i <= num; i += 2)
    {
        if(num % i == 0)
        return false;
    }
    return true;
}

