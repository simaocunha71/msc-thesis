    if(n<2) return false;
    if(n==2) return true;
    if(n%2==0) return false;
    for(int i=3;i*i<=n;i+=2){
        if(n%i==0) return false;
    }
    return true;
}

int main() {
    printf("%d\n", is_prime(6));
    printf("%d\n", is_prime(101));
    printf("%d\n", is_prime(11));
    printf("%d\n", is_prime(13441));
    printf("%d\n", is_prime(61));
    printf("%d\n", is_prime(4));
    printf("%d\n", is_prime(1));
    return 0;
}

