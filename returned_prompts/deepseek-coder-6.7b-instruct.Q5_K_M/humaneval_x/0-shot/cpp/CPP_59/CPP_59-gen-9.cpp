    int i = 2;

B:
    if (n % i == 0){
        n = n / i;
        goto B;
    }
    i++;

C:
    if (i * i > n && n > 1){
        return n;
    }
    if (n > 1){
        goto A;
    }
    return i - 1;
}

int main(){
    printf("%d\n", largest_prime_factor(13195));
    printf("%d\n", largest_prime_factor(2048));
    return 0;
}


*/

