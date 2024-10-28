    vector<int> res;
    if (numbers.size() == 0) return res;
    int max_value = numbers[0];
    res.push_back(max_value);
    for (int i = 1; i < numbers.size(); i++){
        if (numbers[i] > max_value) {
            max_value = numbers[i];
        }
        res.push_back(max_value);
    }
    return res;
}

*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> rolling_max(vector<int> numbers){
    vector<int> res;
    if (numbers.size() == 0) return res;
    int max_value = numbers[0];
    res.push_back(max_value);
    for (int i = 1; i < numbers.size(); i++){
        if (numbers[i] > max_value) {
            max_value = numbers[i];
        }
        res.push_back(max_value);
    }
    return res;
}

int main(){
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i=0; i<result.size(); i++)
        cout<< result[i] << " ";
    return 0;
}
```

This program takes as input a vector of integers and returns a vector where each element is the maximum number found so far in the sequence up to that index.

The program starts by initializing an empty vector for the results. Then it checks if the input vector is empty, if so it returns the empty result vector.

Next, it sets the first element of the input vector as the initial maximum value and pushes it into the result vector. Then it iterates over the remaining elements in the input vector. If it finds a number larger than the current maximum, it updates the maximum and pushes it into the result vector. Otherwise, it just pushes the current maximum into the result vector.

Finally, it returns the result vector.

The