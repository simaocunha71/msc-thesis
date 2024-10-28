    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    float range = max - min;
    for(int i = 0; i < numbers.size(); i++){
        numbers[i] = (numbers[i] - min) / range;
    }
    return numbers;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    numbers = rescale_to_unit(numbers);
    for(int i = 0; i < numbers.size(); i++){
        printf("%f ", numbers[i]);
    }
    return 0;
}


A: I think the problem lies in the way you are using the min_element and max_element functions in your code. The functions return pointers, not the values themselves. Therefore, you should dereference them to get the actual values.

Here is the corrected code:

```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<float> rescale_to_unit(vector<float>& numbers){ 
    float min = *min_element(numbers.begin(), numbers.end());
    float max