    int min_index = min_element(numbers.begin(), numbers.end()) - numbers.begin();
    int max_index = max_element(numbers.begin(), numbers.end()) - numbers.begin();
    float min_value = numbers[min_index];
    float max_value = numbers[max_index];
    float range = max_value - min_value;
    for (int i = 0; i < numbers.size(); i++)
    numbers[i] = (numbers[i] - min_value) / range;
    return numbers;
}


