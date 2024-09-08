    // calculate mean of the dataset
    float sum = 0;
    for(float num : numbers) sum += num;
    float mean = sum / numbers.size();

    // calculate MAD
    float mad = 0;
    for(float num : numbers) mad += abs(num - mean);
    mad /= numbers.size();

    return mad;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    float mad = mean_absolute_deviation(numbers);
    printf("Mean Absolute Deviation: %f\n", mad);
    return 0;
}

C:
    // calculate mean of the dataset
    float sum = 0;
    for(float num : numbers) sum += num;
    float mean = sum / numbers.size();

    // calculate MAD
    float mad = 0;
    for(float num : numbers) mad += abs(num - mean);
    mad /= numbers.size();

    return mad;
}
