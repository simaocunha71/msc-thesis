    // Write your solution here
    for(int i = 2; i <= a; i++){
        if(is_prime(i) && is_prime(a/i) && a%i == 0){
            return true;
        }
    }
    return false;
}
bool is_prime(int a){
    for(int i = 2; i <= a/2; i++){
        if(a%i == 0){
            return false;
        }
    }
    return true;
}
