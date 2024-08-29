/* 
Your task is to write a function that calculates the mean absolute deviation.
To solve this task, you need to implement two functions:
1. float mean(vector<float> numbers)
2. float mean_absolute_deviation(vector<float> numbers)
1. The first function calculates the mean of a given vector of numbers.
2. The second function calculates the mean absolute deviation around the mean of this dataset.
*/
float mean(vector<float> numbers) {
    float sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += numbers[i];
    }
    return sum / numbers.size();
}

float mean_absolute_deviation(vector<float> numbers) {
    float mean_value = mean(numbers);
    float sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += abs(numbers[i] - mean_value);
    }
    return sum / numbers.size();
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("Mean Absolute Deviation: %f\n", mean_absolute_deviation(numbers));
    return 0;
}
B:
/* 
Your task is to write a function that calculates the mean absolute deviation.
To solve this task, you need to implement two functions:
1. float mean(vector<float> numbers)
2. float mean_absolute_deviation(vector<float> numbers)
1. The first function calculates the mean of a given vector of numbers.
2. The second function calculates the mean absolute deviation around the mean of this dataset.
*/
float mean(vector<float> numbers) {
    float sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += numbers[i];
    }
    return sum / numbers.size();
}

float mean_absolute_deviation(vector<float> numbers) {
    float mean_value = mean(numbers);
    float sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += abs(numbers[i] - mean_value);
    }
    return sum / numbers.size();
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("Mean Absolute Deviation: %f\n", mean_absolute_deviation(numbers));
    return 0;
}
C:
/* 
Your task is to write a function that calculates the