    float sum = 0.0; // sum of all numbers
    float sum_squares = 0.0; // sum of squares of all numbers
    float mean; // mean of all numbers
    float mad; // mean absolute deviation
    float total = 0.0; // total absolute deviation
    float avg;

    for (float i : numbers) {
        sum += i;
        sum_squares += pow(i, 2); // pow function calculates the power of a number
    }

    mean = sum / numbers.size(); // calculate the mean

    for (float i : numbers) {
        total += abs(i - mean); // calculate the absolute deviation
    }

    avg = total / numbers.size(); // calculate the mean absolute deviation

    mad = avg;

    return mad;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0}; // input numbers
    float mad = mean_absolute_deviation(numbers); // calculate MAD
    printf("Mean Absolute Deviation = %.1f\n", mad); // print the result
    return 0;
}

C:
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float mean_absolute_deviation(float *numbers, int n) {
    float mean = 0.0;
    float sum = 0.0;
    float total = 0.0;
    float mad = 0.0;

    for (int i = 0; i < n; i++) {
        sum += numbers[i];
    }

    mean = sum / n;

    for (int i = 0; i < n; i++) {
        total += abs(numbers[i] - mean);
    }

    mad = total / n;

    return mad;
}

int main() {
    float numbers[] = {1.0, 2.0, 3.0, 4.0}; // input numbers
    int n = sizeof(numbers) / sizeof(numbers[0]);
    float mad = mean_absolute_deviation(numbers, n); // calculate MAD
    printf("Mean Absolute Deviation = %.1f\n", mad); // print the result
    return 0;
}

Output:
Mean Absolute Deviation = 1.0
*/



