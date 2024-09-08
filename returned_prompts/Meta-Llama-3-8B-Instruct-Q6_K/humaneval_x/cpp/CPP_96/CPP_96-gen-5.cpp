    vector<int> primes;
    if(n <= 1) return primes;
    int i = 2;
    while(i <= n){
        bool isPrime = true;
        for(int j = 2; j * j <= i; j++){
            if(i % j == 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) primes.push_back(i);
        i++;
    }
    return primes;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    vector<int> result = count_up_to(n);
    printf("Prime numbers up to %d: {", n);
    for(int i = 0; i < result.size(); i++){
        printf("%d", result[i]);
        if(i < result.size() - 1) printf(",");
    }
    printf("}\n");
    return 0;
}
