    int i = 2;
    while(i * i <= n){
        if(n % i){
            i++;
        }
        else{
            n /= i;
        }
    }
    return n;
}

int main()
{
    printf("%d\n", largest_prime_factor(13195));
    printf("%d\n", largest_prime_factor(2048));
    return 0;
}
