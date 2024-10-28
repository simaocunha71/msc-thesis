    float min_number = *min_element(numbers.begin(), numbers.end());
    float max_number = *max_element(numbers.begin(), numbers.end());
    float range = max_number - min_number;
    
    for(int i = 0; i < numbers.size(); i++)
        numbers[i] = (numbers[i] - min_number) / range;
    
    return numbers;
}


