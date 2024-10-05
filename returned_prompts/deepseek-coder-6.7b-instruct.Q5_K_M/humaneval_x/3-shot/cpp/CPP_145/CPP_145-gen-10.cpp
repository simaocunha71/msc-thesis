    vector<pair<int, int>> sum_with_index;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        string num_str = to_string(abs(nums[i]));
        for(char c : num_str) sum += c - '0';
        sum_with_index.push_back(make_pair(sum, i));
    }

    sort(sum_with_index.begin(), sum_with_index.end());

    vector<int> result;
    for(auto p : sum_with_index) result.push_back(nums[p.second]);

    return result;
}

