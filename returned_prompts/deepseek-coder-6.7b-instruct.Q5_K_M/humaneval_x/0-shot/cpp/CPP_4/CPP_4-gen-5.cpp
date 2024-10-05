    float sum = 0, mean, mad = 0;
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
    }
    mean = sum / numbers.size();
    for(int i = 0; i < numbers.size(); i++){
        mad += abs(numbers[i] - mean);
    }
    return mad / numbers.size();
}

int main() {
    vector<float> v = {1.0, 2.0, 3.0, 4.0};
    printf("Mean Absolute Deviation: %f\n", mean_absolute_deviation(v));
    return 0;
}

*/

//Problem:
/*
