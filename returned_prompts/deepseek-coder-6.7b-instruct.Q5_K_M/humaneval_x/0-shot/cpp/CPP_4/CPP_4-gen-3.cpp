
The code provided has some syntax issues. Let's correct them.

```cpp
#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

float mean_absolute_deviation(vector<float> numbers){
    float sum = 0.0;
    float mean, mad = 0;
    int i;

    for(i = 0; i < numbers.size(); i++){
        sum += numbers[i];
    }

    mean = sum / numbers.size();

    for(i = 0; i < numbers.size(); i++){
        mad += abs(numbers[i] - mean);
    }

    mad = mad / numbers.size();

    return mad;
}

int main(){

    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    cout << "Mean Absolute Deviation: " << mean_absolute_deviation(numbers) << endl;

    return 0;
}
```

In this corrected code, the function `mean_absolute_deviation` is defined to calculate the mean absolute deviation of a vector of floating point numbers. It first calculates the mean of the numbers, then calculates the absolute difference between each number and the mean, and finally calculates the average of these absolute differences.

In the `main