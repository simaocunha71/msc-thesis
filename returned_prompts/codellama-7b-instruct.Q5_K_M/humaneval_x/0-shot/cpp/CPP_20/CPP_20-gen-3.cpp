    vector<float> result;
    float min_difference = FLT_MAX;
    for(int i = 0; i < numbers.size() - 1; i++){
        for(int j = i + 1; j < numbers.size(); j++){
            float difference = abs(numbers[i] - numbers[j]);
            if(difference < min_difference){
                min_difference = difference;
                result.clear();
                result.push_back(numbers[i]);
                result.push_back(numbers[j]);
            }
            else if(difference == min_difference)
                result.push_back(numbers[j]);
        }
    }
    return result;
}

