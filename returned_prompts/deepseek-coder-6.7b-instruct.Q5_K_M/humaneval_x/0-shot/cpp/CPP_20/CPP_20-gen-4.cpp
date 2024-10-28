    sort(numbers.begin(), numbers.end());
    int size = numbers.size();
    float min_diff = FLT_MAX;
    vector<float> result;
    for(int i = 0; i < size - 1; i++){
        float diff = numbers[i+1] - numbers[i];
        if(diff < min_diff){
            min_diff = diff;
            result.clear();
            result.push_back(numbers[i]);
            result.push_back(numbers[i+1]);
        }
    }
    return result;
}

int main() {

    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest = find_closest_elements(numbers);
    printf("(%f, %f)\n", closest[0], closest[1]);

    return 0;
}


A: The algorithm you're looking for is called "Sort and Scan". Here's the modified version of your code that implements "Sort and Scan" algorithm:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cfloat>
using namespace std;

pair<float, float> find_closest_elements(vector<float> numbers){
    sort(numbers.begin(), numbers.end());
    int size = numbers.size();
    float min_diff = FLT_MAX;
    pair<float, float> result;
    for(int i = 0; i < size - 1; i++){
        float diff = numbers[i+1] - numbers[i];
        if(diff < min_diff){
            min_diff = diff;
            result = make_pair(numbers[i], numbers[i+1]);
        }
    }
    return result;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    pair<float, float> closest = find