    vector<pair<int, int>> pairs;
    int sum;
    for (int i = 0; i < nums.size(); i++) {
        sum = 0;
        string num_str = to_string(abs(nums[i]));
        for (char c : num_str) {
            sum += c - '0';
        }
        pairs.push_back(make_pair(sum, nums[i]));
    }
    sort(pairs.begin(), pairs.end());
    vector<int> res;
    for (pair<int, int> p : pairs) {
        res.push_back(p.second);
    }
    return res;
}


