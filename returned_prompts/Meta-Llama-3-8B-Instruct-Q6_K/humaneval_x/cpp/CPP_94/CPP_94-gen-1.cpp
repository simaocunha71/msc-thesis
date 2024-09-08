The code provided is almost correct but it's missing the necessary header files and namespace declaration. Here's the corrected code:

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int skjkasdkd(vector<int> lst) {
    int max_prime = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] > max_prime && isPrime(lst[i])){
            max_prime = lst[i];
        }
    }
    int sum = 0;
    int temp = max_prime;
    while(temp > 0){
        sum += temp % 10;
        temp /= 10;
    }
    return sum;
}

int main() {
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5