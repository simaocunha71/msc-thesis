    float sum = 0;
    float mean = 0;
    float mad = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += numbers[i];
    }
    mean = sum / numbers.size();
    for (int i = 0; i < numbers.size(); i++) {
        mad += abs(numbers[i] - mean);
    }
    mad /= numbers.size();
    return mad;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%f\n", mean_absolute_deviation(numbers));
    return 0;
}
