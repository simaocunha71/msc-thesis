    // Calculate mean of the input numbers
    float sum = 0.0;
    for(float num : numbers){
        sum += num;
    }
    float mean = sum / numbers.size();

    // Calculate Mean Absolute Deviation
    float mad = 0.0;
    for(float num : numbers){
        mad += abs(num - mean);
    }
    mad /= numbers.size();

    return mad;
}
int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    float mad = mean_absolute_deviation(numbers);
    printf("Mean Absolute Deviation is %f\n", mad);
    return 0;
}

C:
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 4

int main() {
    float numbers[N] = {1.0, 2.0, 3.0, 4.0};
    float sum = 0.0;
    float mad = 0.0;

    // Calculate mean of the input numbers
    for(int i = 0; i < N; i++) {
        sum += numbers[i];
    }
    float mean = sum / N;

    // Calculate Mean Absolute Deviation
    for(int i = 0; i < N; i++) {
        mad += fabs(numbers[i] - mean);
    }
    mad /= N;

    printf("Mean Absolute Deviation is %f\n", mad);

    return 0;
}
// Output: Mean Absolute Deviation is 1.000000
C++ code snippet:

```cpp
#include <iostream>
#include <vector>
#include <cmath>

float mean_absolute_deviation(const std::vector<float>& numbers) {
    float sum = 0.0;
    float mad = 0.0;

    // Calculate mean of the input numbers
    for (const auto& num : numbers) {
        sum += num;
    }
    float mean = sum / numbers.size();

    // Calculate Mean Absolute Deviation
    for (const auto& num : numbers) {
        mad += std::abs(num - mean);
    }
    mad /= numbers.size();

    return mad;
}

int main() {
    std::vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    float mad = mean_absolute_deviation(numbers);
    std::cout << "Mean Absolute Deviation