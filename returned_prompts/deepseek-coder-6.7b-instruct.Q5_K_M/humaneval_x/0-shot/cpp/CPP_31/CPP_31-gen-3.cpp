    if(n<=1)
        return false;
    if(n==2 || n==3)
        return true;
    if(n%2==0 || n%3==0)
        return false;

B:
    for(long long i=5; i*i<=n; i+=6){
        if(n%i==0 || n%(i+2)==0)
            return false;
    }

    return true;
}
int main(){
    long long n;
    scanf("%lld",&n);
    is_prime(n)?printf("true"):printf("false");
    return 0;
}
*/

// Test Cases
// 6 -> false
// 101 -> true
// 11 -> true
// 13441 -> true
// 61 -> true
// 4 -> false
// 1 -> false
// 2 -> true
// 3 -> true
// 49 -> false
// 97 -> true
// 100 -> false
// 1000000007 -> true
// 1373653 -> true
// 4879 -> true
// 839284 -> true
// 2147483647 -> true
// 2147483646 -> false
// 13441 -> true
// 987654321 -> true
// 987654320 -> false
// 1000000000 -> false
// 1000000001 -> true
// 1000000002 -> true

// This is a simple implementation of the Sieve of Eratosthenes algorithm, which is used to find all primes less than a given number n.
// It works by iteratively marking the multiples of numbers, starting from 2, as composite (not prime). The remaining unmarked numbers in the list are primes.
// This