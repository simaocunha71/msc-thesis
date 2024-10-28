    vector<int> result(n);
    for(int i=1; i<=n; ++i){
        if(i%2 == 0){
            int fact = 1;
            for(int j=1; j<=i; ++j) fact *= j;
            result[i-1] = fact;
        }else{
            int sum = 0;
            for(int j=1; j<=i; ++j) sum += j;
            result[i-1] = sum;
        }
    }
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> result = f(n);
    for(int i=0; i<result.size(); ++i){
        printf("%d ", result[i]);
    }
    return 0;
}

*/

// Solution
#include <iostream>
#include <vector>

using namespace std;

int factorial(int n) {
    int fact = 1;
    for(int i = 1; i <= n; i++) {
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
    vector<int> result(n);
    for(int i = 0; i < n; i++) {
        if(i % 2 == 0) {
            result[i] = factorial(i);
        } else {
            result[i] = sum(i);
        }
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> result = f(n);
    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}

/*
Explanation:
The function `f` is implemented such that