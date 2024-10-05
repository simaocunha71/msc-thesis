    for(int i = 2; i <= sqrt(a); i++){
        if(a%i == 0){
            int b = a/i;
            int c = b/i;
            if(is_prime(i) && is_prime(b) && is_prime(c))
                return true;
        }
    }
    return false;
}

bool is_prime(int a){
    if(a <= 1) return false;
    for(int i = 2; i <= sqrt(a); i++){
        if(a%i == 0)
            return false;
    }
    return true;
}