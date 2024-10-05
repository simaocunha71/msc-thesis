    vector<int> factors;
    // Start from 2, because 1 is not prime
    for(int i = 2; i <= n; i++){
        // if n is divisible by i, then it's a factor
        while(n % i == 0){
            factors.push_back(i);
            // divide n by i so we can find next factor
            n /= i;
        }
    }
    return factors;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    vector<int> factors = factorize(n);
    printf("Prime factors are: ");
    for(int i = 0; i < factors.size(); i++){
        printf("%d ", factors[i]);
    }
    return 0;
}
*/

/*
The function factorize(int n) works by dividing the input number n by integers i starting from 2, and checking if n is divisible by i. If n is divisible by i, then i is a factor of n, and we divide n by i to find the next factor. This process continues until n is no longer divisible by i. The factors are stored in a vector and returned by the function.
*/

//