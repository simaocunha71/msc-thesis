    vector<int> max_values;
    int max = INT_MIN;
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
        max_values.push_back(max);
    }
    return max_values;
} 

