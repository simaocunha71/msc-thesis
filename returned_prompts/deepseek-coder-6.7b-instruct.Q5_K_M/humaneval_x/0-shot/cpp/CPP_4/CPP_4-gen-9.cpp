float mean_absolute_deviation(vector<float> numbers){
    float sum = 0.0, mean, mad = 0.0;

    // Calculate the mean of the numbers
    for(int i = 0; i < numbers.size(); ++i)
        sum += numbers[i];
    mean = sum/numbers.size();

    // Calculate the Mean Absolute Deviation
    for(int i = 0; i < numbers.size(); ++i)
        mad += abs(numbers[i] - mean);
    mad = mad/numbers.size();

    return mad;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("Mean Absolute Deviation: %f", mean_absolute_deviation(numbers));
    return 0;
}

/*
Output:
Mean Absolute Deviation: 1.000000
*/

// The program calculates the mean absolute deviation of the numbers 1.0, 2.0, 3.0, and 4.0, which is 1.0.
// This is because the mean of the numbers is 2.5, and the absolute deviation from this mean for each number is 1.0, 0