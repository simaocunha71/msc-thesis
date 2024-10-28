    float sum = 0;
    for (int i = 0; i < numbers.size(); i++)
    {
        sum += abs(numbers[i] - numbers[numbers.size()/2]);
    }
    return sum/numbers.size();
}
int main() {
    vector<float> numbers;
    numbers.push_back(1.0);
    numbers.push_back(2.0);
    numbers.push_back(3.0);
    numbers.push_back(4.0);
    float answer = mean_absolute_deviation(numbers);
    printf("%f\n", answer);
    return 0;
}

