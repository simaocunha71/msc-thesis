    vector<int> result;
    int max_element = INT_MIN;

    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] > max_element){
            max_element = numbers[i];
        }
        result.push_back(max_element);
    }
    return result;
}
