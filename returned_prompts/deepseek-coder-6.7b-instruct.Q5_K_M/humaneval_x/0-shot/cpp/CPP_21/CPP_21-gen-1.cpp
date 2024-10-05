    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    float range = max - min;

    for (int i=0; i<numbers.size(); i++){
        numbers[i] = (numbers[i] - min) / range;
    }
    return numbers;
}

/*
