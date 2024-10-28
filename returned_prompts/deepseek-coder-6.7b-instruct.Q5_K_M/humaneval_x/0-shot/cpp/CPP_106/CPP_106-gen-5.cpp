    vector<int> vec;
    for(int i=1; i<=n; i++){
        if(i%2 == 0){
            int fact = 1;
            for(int j=1; j<=i; j++){
                fact *= j;
            }
            vec.push_back(fact);
        } else {
            int sum = 0;
            for(int j=1; j<=i; j++){
                sum += j;
            }
            vec.push_back(sum);
        }
    }
    return vec;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> result = f(n);
    for (int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    return 0;
}

The code above uses C++ and it computes the factorial and the sum as requested. It uses a for loop to iterate over the numbers from 1 to n and inside this loop it computes the factorial or the sum of the numbers from 1 to i and then it pushes back the computed value into the vector. Finally it returns the vector.
*/

#include <iostream>
#include <vector>
using namespace std;

int factorial(int n) {
    int fact = 1;
    for(int i = 2; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int sum(int n) {
    int sum = 0;
    for(int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

vector<int> f(int n) {
    vector<int> result;
    for(int i = 1; i <= n; i++) {
        if(i % 2 == 0) {
            result.push_back(factorial(i));
        } else {
            result.push_back(sum(i));
        }
    }
    return result;
}

int main() {