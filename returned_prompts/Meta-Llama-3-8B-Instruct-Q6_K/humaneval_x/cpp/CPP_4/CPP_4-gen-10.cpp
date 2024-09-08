    float mean = 0;
    float sum = 0;
    int n = numbers.size();
    for(int i = 0; i < n; i++){
        sum += numbers[i];
    }
    mean = sum / n;

    float mad = 0;
    for(int i = 0; i < n; i++){
        mad += abs(numbers[i] - mean);
    }
    mad /= n;

    return mad;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%f\n", mean_absolute_deviation(numbers));
    return 0;
}
C++:

Here is a simple implementation of the Mean Absolute Deviation (MAD) function in C++. This function takes a vector of float numbers as an input and returns the Mean Absolute Deviation around the mean of this dataset. The Mean Absolute Deviation is calculated as the average absolute difference between each element and the mean of the dataset.

The function first calculates the mean of the dataset by summing up all the elements and dividing by the number of elements. Then, it calculates the Mean Absolute Deviation by summing up the absolute differences between each element and the mean and dividing by the number of elements.

In the main function, we create a vector of float numbers and pass it to the Mean Absolute Deviation function. The result is then printed to the console.

```c
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

float mean_absolute_deviation(vector<float> numbers) {
    float mean = 0;
    float sum = 0;
    int n = numbers.size();
    for(int i = 0; i < n; i++){
        sum += numbers[i];
    }
    mean = sum / n;

    float mad = 0;
    for(int i = 0; i < n; i++){
        mad += abs(numbers[i] - mean);
    }
    mad /= n;

    return mad;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    cout << mean_absolute_deviation(numbers) << endl;
    return 0;
}
```

Output:

```
1.000000
```

This output is correct, as the Mean Absolute Deviation for the dataset {1.0, 2.0, 3.0, 4.0