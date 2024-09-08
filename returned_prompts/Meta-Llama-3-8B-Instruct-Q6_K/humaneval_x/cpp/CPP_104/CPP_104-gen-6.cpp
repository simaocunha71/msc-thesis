    vector<int> res;
    for(int i = 0; i < x.size(); i++){
        int num = x[i];
        bool has_even = false;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                has_even = true;
                break;
            }
            num /= 10;
        }
        if(!has_even){
            res.push_back(x[i]);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
//Output:
//1 15 33

B:
Here is the C++ code for the problem:
```
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

vector<int> unique_digits(vector<int> x) {
    vector<int> res;
    for (int num : x) {
        bool has_even = false;
        for (int digit : to_string(num)) {
            if (stoi(digit) % 2 == 0) {
                has_even = true;
                break;
            }
        }
        if (!has_even) {
            res.push_back(num);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main() {
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
```
This code uses the `to_string` function to convert each integer in the input vector to a string, and then iterates over each character (digit) in the string to check if it's even. If no even digits are found, the number is added to the result vector. Finally, the result vector is sorted and returned. The `main` function demonstrates the usage of the `unique_digits` function.

This solution has a time complexity of O(n*m), where n is the size of the input vector and m is the maximum number of digits in an integer in the input vector. This is because we