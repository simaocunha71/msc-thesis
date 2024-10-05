    vector<int> res(n);
    for(int i=1; i<=n; i++){
        int fact = 1;
        int sum = 0;
        if(i%2==0){
            for(int j=1; j<=i; j++){
                fact*=j;
            }
            res[i-1] = fact;
        }else{
            for(int j=1; j<=i; j++){
                sum+=j;
            }
            res[i-1] = sum;
        }
    }
    return res;
}

int main() {
    int n = 5;
    vector<int> result = f(n);
    for(int i = 0; i < n; i++) {
        printf("%d ", result[i]);
    }
    return 0;
}

The function f first initializes a vector of size n filled with 0s. Then it runs a loop from 1 to n (inclusive). Inside the loop, it checks if i is even. If i is even, it calculates the factorial of i and stores it in the i-th element of the vector (with 0-based indexing). If i is not even, it calculates the sum of numbers from 1 to i and stores it in the i-th element of the vector. Finally, it returns the vector.
*/

// Your code should be similar to this.

#include <iostream>
#include <vector>
using namespace std;

vector<int> f(int n){
    vector<int> res(n);
    for(int i=1; i<=n; i++){
        int fact = 1;
        int sum = 0;
        if(i%2==0){
            for(int j=1; j<=i; j++){
                fact*=j;
            }
            res[i-1] = fact;
        }else{
            for(int j=1; j<=i; j++){
                sum+=j;
            }
            res[i-1] = sum;
        }
    }
    return res;
}