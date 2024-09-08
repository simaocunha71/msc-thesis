    vector<int> result;
    if(n < 2) return result;
    result.push_back(2);
    for(int i = 3; i < n; i+=2){
        bool isPrime = true;
        for(int j = 3; j*j <= i; j+=2){
            if(i % j == 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) result.push_back(i);
    }
    return result;
}
int main()
{
    printf("%lu\n",(long)count_up_to(5).size());
    printf("%lu\n",(long)count_up_to(11).size());
    printf("%lu\n",(long)count_up_to(0).size());
    printf("%lu\n",(long)count_up_to(20).size());
    printf("%lu\n",(long)count_up_to(1).size());
    printf("%lu\n",(long)count_up_to(18).size());

    return 0;
}
B:
The function count_up_to(n) returns a vector of all prime numbers less than or equal to n.
Here is the improved function:
```cpp
#include<vector>
#includealgorithm>
using namespace std;

vector<int> count_up_to(int n) {
    vector<int> result;
    for (int i = 2; i <= n; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            result.push_back(i);
        }
    }
    return result;
}
```
Explanation:
The function count_up_to(n) iterates over all integers from 2 to n (inclusive) and checks if each integer is prime. If the integer is prime, it is added to the result vector.
The function starts from 2 because 2 is the smallest prime number. It iterates over all integers up to n, and for each integer, it checks if it is prime by iterating over all integers from 2 to the square root of the current integer. If the current integer is divisible by any of these integers, it is not prime and the loop is terminated. If the current integer is not divisible by any of these integers, it is prime and it is added to the result vector.
The function returns the result vector which contains all prime numbers less than