    float min = numbers[0];
    float max = numbers[0];
    for (int i = 0; i < numbers.size(); i++) {
        if (min > numbers[i]) {
            min = numbers[i];
        }
        if (max < numbers[i]) {
            max = numbers[i];
        }
    }
    for (int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min) / (max - min);
    }
    return numbers;
}

vector<float> res = rescale_to_unit({1.0, 2.0, 3.0, 4.0, 5.0});
for (int i = 0; i < res.size(); i++) {
    printf("%f ", res[i]);
}


ANSWER:
Here's a function that takes a vector of numbers and applies a linear transform to rescale the smallest number to 0 and the largest number to 1:

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers) {
    float min = numbers[0];
    float max = numbers[0];
    for (int i = 0; i < numbers.size(); i++) {
        if (min > numbers[i]) {
            min = numbers[i];
        }
        if (max < numbers[i]) {
            max = numbers[i];
        }
    }
    for (int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min) / (max - min);
    }
    return numbers;
}

int main() {
    vector<float> res = rescale_to_unit({1.0, 2.0, 3.0, 4.0, 5.0});
    for (int i = 0; i < res.size(); i++) {
        printf("%f ", res[i]);
    }
    return