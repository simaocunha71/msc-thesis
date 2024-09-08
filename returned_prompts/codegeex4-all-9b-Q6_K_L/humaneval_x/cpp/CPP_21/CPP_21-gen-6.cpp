vector<float> rescale_to_unit(vector<float> numbers) { 
    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min) / (max - min);
    }
    return numbers;
}