    vector<bool> prime(n+1, true);
    prime[0] = prime[1] = false;
    for (int i = 2; i * i <= n; i++){
        if (prime[i] == true){
            for (int j = i * i; j <= n; j += i)
                prime[j] = false;
        }
    }

B:
    vector<int> result;
    for (int i = 2; i <= n; i++){
        if (prime[i]){
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    vector<int> v;
    v = count_up_to(20);
    for(int i = 0; i < v.size(); i++){
        printf("%d ",v[i]);
    }
    return 0;
}

This program works by using the Sieve of Eratosthenes algorithm to find all the prime numbers up to n. The Sieve of Eratosthenes algorithm is an efficient way to find all primes smaller than n when n is smaller than 10 million.

The Sieve of Eratosthenes works by iteratively marking the multiples of numbers starting from 2, the first prime number. The remaining unmarked numbers in the list are primes.

A: This part of the program creates an array of boolean values, prime, initialized as true for all indices from 0 to n. It then iteratively marks the multiples of each number starting from 2 as false, indicating they are not prime.

B: This part of the program creates a vector, result, to store the prime numbers. It then iterates over the prime array and if a number is marked as true (indicating it is prime), it is added to the result vector. Finally, the result vector is returned.

The time complexity of this program is O(n log log n) due to the Sieve of Eratosthenes algorithm.
*/


// 2019012922 이용훈
// 정보보안과 게임