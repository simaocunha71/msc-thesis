    float mean = 0;
    for(int i = 0; i < numbers.size(); i++){
        mean += numbers[i];
    }
    mean /= numbers.size();
    float mad = 0;
    for(int i = 0; i < numbers.size(); i++){
        mad += abs(numbers[i] - mean);
    }
    mad /= numbers.size();
    return mad;
}
int main() {
    vector<float> numbers{1.0, 2.0, 3.0, 4.0};
    printf("%f", mean_absolute_deviation(numbers));
    return 0;
}

