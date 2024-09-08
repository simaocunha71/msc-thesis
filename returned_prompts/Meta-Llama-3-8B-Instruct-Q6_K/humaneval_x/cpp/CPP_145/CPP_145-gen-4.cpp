    // Create a map to store the sum of digits and the corresponding index in the original vector
    map<int, pair<int, int>> map;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int temp = nums[i];
        while(temp != 0){
            sum += temp % 10;
            temp /= 10;
        }
        map[sum].first = sum;
        map[sum].second = i;
    }
    // Create a vector to store the sorted result
    vector<int> result;
    for(auto it = map.rbegin(); it != map.rend(); ++it){
        for(int i = it->second; i < nums.size(); i++){
            if(map.find(sum) != map.end()){
                result.push_back(nums[i]);
                map.erase(sum);
            }
        }
    }
    return result;
}

B:
    // Create a vector to store the result
    vector<int> result;
    // Sort the vector based on the sum of digits and index
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int temp = nums[i];
        while(temp != 0){
            sum += temp % 10;
            temp /= 10;
        }
        result.push_back({sum, i});
    }
    sort(result.begin(), result.end());
    // Create a vector to store the sorted result
    vector<int> result;
    for(int i = 0; i < result.size(); i++){
        result.push_back(result[i].second);
    }
    return result;
}

C:
    // Create a map to store the sum of digits and the corresponding index in the original vector
    map<int, int> map;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int temp = nums[i];
        while(temp != 0){
            sum += temp % 10;
            temp /= 10;
        }
        map[sum].push_back(i);
    }
    // Create a vector to store the sorted result
    vector<int> result;
    for(auto it = map.rbegin(); it != map.rend(); ++it){
        for(auto it2 = it->second.begin(); it2 != it->second.end(); ++it2){
            result.push_back(nums[*it2]);
        }
    }
    return result;
}
D:
    // Create