    if (n <= 1){
        return false;
    }
    else if (n <= 3){
        return true;
    }
    else if (n % 2 == 0 || n % 3 == 0){
        return false;
    }
    long long i = 5;
    while (i * i <= n){
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
        i += 6;
    }
    return true;
}

int main(){
    long long n;
    scanf("%lld", &n);
    if(is_prime(n)){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}

