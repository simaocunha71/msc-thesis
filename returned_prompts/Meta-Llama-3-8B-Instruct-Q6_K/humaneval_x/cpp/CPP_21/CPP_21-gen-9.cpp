    vector<float> result;
    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    for(float x : numbers){
        result.push_back((x - min) / (max - min));
    }
    return result;
}
