    vector<int> result;
    for(int i = 2; i <= n; i++){
        int count = 0;
        while(n % i == 0){
            n /= i;
            count++;
        }
        if(count > 0){
            result.push_back(i);
            result.insert(result.end(), count, i);
        }
    }
    if(n > 1){
        result.push_back(n);
    }
    return result;
}

int main(){
    printf("%s\n", (factorize(8)).c_str());
    printf("%s\n", (factorize(25)).c_str());
    printf("%s\n", (factorize(70)).c_str());
    return 0;
}
R:

```c
#include <iostream>
#include <vector>

using namespace std;

vector<int> factorize(int n) {
    vector<int> result;
    for (int i = 2; i <= n; i++) {
        int count = 0;
        while (n % i == 0) {
            n /= i;
            count++;
        }
        if (count > 0) {
            result.push_back(i);
            result.insert(result.end(), count, i);
        }
    }
    if (n > 1) {
        result.push_back(n);
    }
    return result;
}

int main() {
    vector<int> res1 = factorize(8);
    vector<int> res2 = factorize(25);
    vector<int> res3 = factorize(70);

    for (int i : res1) {
        cout << i << " ";
    }
    cout << endl;

    for (int i : res2) {
        cout << i << " ";
    }
    cout << endl;

    for (int i : res3) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
```

The code uses a loop to iterate over all numbers from 2 to the input number. For each number, it checks if the input number is divisible by the current number. If it is, it divides the input number by the current number and increments a counter. After the loop, it checks if the input number is greater than 1, which means it's a prime number. If it is, it adds the prime number to the result vector.

The result vector contains the prime factors of the input number, each repeated the number of times it appears in the factorization. The order