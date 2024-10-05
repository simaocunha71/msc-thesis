    vector<int> result;
    if(n<2) return result;
    bool isPrime[n+1];
    for(int i=0;i<=n;i++) isPrime[i]=true;

B:
    for(int i=2;i*i<=n;i++){
        if(isPrime[i]==true){
            for(int j=i*i;j<=n;j+=i) isPrime[j]=false;
        }
    }

C:
    for(int i=2;i<n;i++){
        if(isPrime[i]) result.push_back(i);
    }

    return result;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    vector<int> primes = count_up_to(n);
    printf("Prime numbers up to %d are: ",n);
    for(int i=0;i<primes.size();i++) printf("%d ",primes[i]);
    return 0;
}

//Time Complexity: O(n log log n)
//Space Complexity: O(n)

/*
Explanation:
A: Initialize a boolean array "isPrime[0..n]" and set all entries as true. A value in isPrime[i] will finally be false if i is Not a prime, otherwise true.
B: Traverse through the numbers from 2 to sqrt(n) and if isPrime[i] is true then mark all multiples of i as not prime.
C: Traverse through the boolean array and if isPrime[i] is true then push i into the result vector.
*/

//This function uses the Sieve of Eratosthenes algorithm which is one of the most efficient ways to find all primes smaller than n when n is smaller than or equal to 10 million.

//It's a bit hard to understand at first but once you understand it, it's a really efficient way to find all primes smaller than n.

//Also, it's a good