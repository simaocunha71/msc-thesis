    vector<int> res;
    if(numbers.empty()) return res;

B:
    int max_val = numbers[0];
    res.push_back(max_val);

C:
    for(int i = 1; i < numbers.size(); i++){
        if(numbers[i] > max_val){
            max_val = numbers[i];
        }
        res.push_back(max_val);
    }

D:
    return res;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> res = rolling_max(numbers);
    for(int i = 0; i < res.size(); i++) {
        printf("%d ", res[i]);
    }
    return 0;
}
*/

R:
The function rolling_max generates a vector of integers by comparing each element in the input vector with the previous maximum value. If the current element is greater than the maximum value, it updates the maximum value. The maximum value is then pushed back into the result vector. If the input vector is empty, the function returns an empty result vector.
The main function tests the rolling_max function by passing it a vector of integers, then prints the result vector to the console.
*/

#include<stdio.h>
#include<vector>
using namespace std;

vector<int> rolling_max(vector<int> numbers){
    vector<int> res;
    if(numbers.empty()) return res;

    int max_val = numbers[0];
    res.push_back(max_val);

    for(int i = 1; i < numbers.size(); i++){
        if(numbers[i] > max_val){
            max_val = numbers[i];
        }
        res.push_back(max_val);
    }

    return res;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> res = rolling_max(