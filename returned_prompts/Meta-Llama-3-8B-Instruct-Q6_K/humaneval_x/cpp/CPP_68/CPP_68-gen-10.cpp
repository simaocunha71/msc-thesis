    vector<int> result;
    int smallest_value = INT_MAX;
    int smallest_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < smallest_value){
            smallest_value = arr[i];
            smallest_index = i;
        }
    }
    if(smallest_value == INT_MAX){
        return {};
    }
    result.push_back(smallest_value);
    result.push_back(smallest_index);
    return result;
}  // Time Complexity O(n) and Space Complexity O(1) 

B:
    vector<int> result;
    int smallest_value = INT_MAX;
    int smallest_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < smallest_value){
            smallest_value = arr[i];
            smallest_index = i;
        }
        else if(arr[i] % 2 == 0 && arr[i] == smallest_value){
            smallest_index = i;
        }
    }
    if(smallest_value == INT_MAX){
        return {};
    }
    result.push_back(smallest_value);
    result.push_back(smallest_index);
    return result;

}  // Time Complexity O(n) and Space Complexity O(1) 

C:
    vector<int> result;
    int smallest_value = INT_MAX;
    int smallest_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0){
            if(arr[i] < smallest_value){
                smallest_value = arr[i];
                smallest_index = i;
            }
            else if(arr[i] == smallest_value){
                smallest_index = i;
            }
        }
    }
    if(smallest_value == INT_MAX){
        return {};
    }
    result.push_back(smallest_value);
    result.push_back(smallest_index);
    return result;

}  // Time Complexity O(n) and Space Complexity O(1) 

D:
    vector<int> result;
    int smallest_value = INT_MAX;
    int smallest_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0){
            if(arr[i] < smallest_value){
                smallest_value = arr[i];
                smallest_index = i;
            }
            else if(arr[i] == smallest_value){
                smallest_index =