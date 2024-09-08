    vector<float> result;
    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());
    
    for(float num : numbers){
        result.push_back((num - min_val) / (max_val - min_val));
    }
    return result;
}

