    float sum = 0;
    for(int i=0; i<numbers.size(); i++)
        sum += numbers[i];
    float mean = sum/numbers.size();
    float mad = 0;
    for(int i=0; i<numbers.size(); i++)
        mad += abs(numbers[i] - mean);
    return mad/numbers.size();
}
int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("Mean Absolute Deviation: %f\n", mean_absolute_deviation(numbers));
    return 0;
}
```

The program calculates the mean of the input numbers, then for each number, it subtracts the mean and takes the absolute value. It adds these absolute differences together and then divides by the size of the input vector to get the Mean Absolute Deviation.

Note: This program uses C++ and the Standard Template Library (STL).


## Testing

Here is an example of how you might test this function:

```C++
#include <vector>
#include <cassert>

int main() {
    {
        std::vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
        assert(mean_absolute_deviation(numbers) == 1.0);
    }
    {
        std::vector<float> numbers = {5.0, 10.0, 15.0, 20.0};
        assert(mean_absolute_deviation(numbers) == 7.5);
    }
    {
        std::vector<float> numbers = {0.0, 0.0, 0.0, 0.0};
        assert(mean_absolute_deviation(numbers) == 0.0);
    }
    return 0;
}
```

These tests check that the function works correctly with a variety of different input vectors.


## Complexity

The time complexity of this program is O(n) because it iterates over the input