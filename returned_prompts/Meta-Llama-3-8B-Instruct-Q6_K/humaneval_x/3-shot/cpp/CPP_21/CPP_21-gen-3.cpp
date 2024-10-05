    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());
    vector<float> scaled_numbers;
    for (float num : numbers) {
        scaled_numbers.push_back((num - min_val) / (max_val - min_val));
    }
    return scaled_numbers;
} 
*/



