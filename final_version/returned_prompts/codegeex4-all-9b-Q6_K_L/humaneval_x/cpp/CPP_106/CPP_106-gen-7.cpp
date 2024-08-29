#include <iostream>
#include <vector>
using namespace std;

vector<int> f(int n){
    vector<int> result(n);
    int factorial = 1;
    int sum = 0;
    for(int i = 0; i < n; ++i){
        if(i % 2 == 0){
            factorial *= i;
            result[i] = factorial;
        } else {
            sum += i;
            result[i] = sum;
        }
    }
    return result;
}

int main() {
    vector<int> output = f(5);
    for(int i = 0; i < output.size(); ++i){
        cout << output[i] << " ";
    }
    cout << endl;
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

vector<int> f(int n){
    vector<int> result(n);
    for(int i = 1; i <= n; ++i){
        if(i % 2 == 0){
            int factorial = 1;
            for(int j = 1; j <= i; ++j){
                factorial *= j;
            }
            result[i-1] = factorial;
        } else {
            int sum = 0;
            for(int j = 1; j <= i; ++j){
                sum += j;
            }
            result[i-1] = sum;
        }
    }
    return result;
}

int main() {
    vector<int> output = f(5);
    for(int i = 0; i < output.size(); ++i){
        cout << output[i] << " ";
    }
    cout << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
using namespace std;

vector<int> f(int n){
    vector<int> result(n);
    for(int i = 0; i < n; ++i){
        if(i % 2 == 0){
            result[i] = 1;
            for(int j = 1; j <= i; ++j){
                result[i] *= j;
            }
        } else {
            result[i] = 0;
            for(int j = 1; j <= i; ++j){
                result[i] += j;
            }
        }
    }
    return result;
}

int main() {
    vector<int> output = f(5);
    for(int i = 0; i < output.size(); ++i){
        cout << output