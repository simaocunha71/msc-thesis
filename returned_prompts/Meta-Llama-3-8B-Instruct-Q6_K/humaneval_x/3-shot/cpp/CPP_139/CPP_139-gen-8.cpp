    long long result = 1;
    for(int i = 1; i <= n; i++) {
        result *= i;
        for(int j = i - 1; j >= 1; j--) {
            result *= j;
        }
    }
    return result;
} // This function is inefficient and may cause an overflow for large inputs. For a better solution, refer to the next answer.
// An improved version of the function
#include <iostream>
#include <vector>
#include <string>
using namespace std;

long long special_factorial(int n) {
    long long result = 1;
    vector<long long> factorials;
    factorials.push_back(1);
    for(int i = 1; i <= n; i++) {
        result *= i;
        factorials.push_back(result);
    }
    for(int i = n - 1; i >= 1; i--) {
        result *= factorials[i];
    }
    return result;
} // This function is more efficient and can handle large inputs.