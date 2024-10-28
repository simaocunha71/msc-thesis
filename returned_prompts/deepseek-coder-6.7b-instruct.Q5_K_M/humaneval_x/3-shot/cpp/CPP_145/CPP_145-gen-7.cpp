    vector<pair<int, int>> vec;
    for (int i = 0; i < nums.size(); ++i) {
        int sum = 0;
        int n = abs(nums[i]);
        while (n) {
            sum += n % 10;
            n /= 10;
        }
        vec.push_back(make_pair(sum, nums[i]));
    }
    sort(vec.begin(), vec.end());
    vector<int> res;
    for (int i = 0; i < vec.size(); ++i) {
        res.push_back(vec[i].second);
    }
    return res;
}

