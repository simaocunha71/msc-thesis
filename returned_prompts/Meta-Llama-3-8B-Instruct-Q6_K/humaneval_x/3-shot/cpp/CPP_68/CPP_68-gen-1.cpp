    vector<int> result;
    if(arr.empty()) return result;
    int min_even_index = -1, min_even_value = INT_MAX;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] % 2 == 0 && arr[i] < min_even_value) {
            min_even_value = arr[i];
            min_even_index = i;
        }
    }
    if(min_even_index != -1) {
        result.push_back(min_even_value);
        result.push_back(min_even_index);
    } else {
        result.push_back({});
        result.push_back({});
    }
    return result;
}  