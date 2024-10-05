    float sum = 0;
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
    }
    float mean = sum/numbers.size();
    float mad = 0;
    for(int i = 0; i < numbers.size(); i++){
        mad += abs(numbers[i] - mean);
    }
    return mad/numbers.size();
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("Mean Absolute Deviation: %f\n", mean_absolute_deviation(numbers));
    return 0;
}
```

The main program initiates a vector with the given numbers and calculates the mean absolute deviation by calling the function `mean_absolute_deviation()`. The result is printed to the standard output.

In the function `mean_absolute_deviation()`, firstly, it calculates the mean of all numbers by adding them all together and dividing by the quantity of numbers. Then, it calculates the mean absolute deviation by summing all the absolute differences between each number and the mean. Finally, it returns the mean absolute deviation by dividing the sum by the quantity of numbers.

This program uses C++ standard library and math functions, so it should be compiled with a C++ compiler.

It's worth mentioning that this problem could be solved in a more efficient way, but this solution is simple and easy to understand.

Please, let me know if you need anything else.


















































































































































