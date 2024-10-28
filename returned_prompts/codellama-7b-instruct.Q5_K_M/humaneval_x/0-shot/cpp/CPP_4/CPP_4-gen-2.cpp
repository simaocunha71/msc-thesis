    float sum = 0.0;
    float mean = 0.0;
    float absolute_deviation = 0.0;
    float MAD = 0.0;
    float n = numbers.size();
    for(int i = 0; i < n; i++){
        sum = sum + numbers[i];
    }
    mean = sum / n;
    for(int i = 0; i < n; i++){
        absolute_deviation = fabs(numbers[i] - mean);
        MAD = MAD + absolute_deviation;
    }
    MAD = MAD / n;
    return MAD;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%f\n", mean_absolute_deviation(numbers));
    return 0;
}
