    vector<pair<int, int>> v;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        int n = nums[i];
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        v.push_back({sum, i});
    }
    sort(v.begin(), v.end());
    vector<int> res;
    for (int i = 0; i < v.size(); i++) {
        res.push_back(nums[v[i].second]);
    }
    return res;
}