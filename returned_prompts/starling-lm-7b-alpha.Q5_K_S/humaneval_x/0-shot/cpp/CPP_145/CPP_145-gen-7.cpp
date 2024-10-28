    vector<int> res;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        while (nums[i]) {
            sum += nums[i] % 10;
            nums[i] /= 10;
        }
        res.push_back(sum);
    }
    // sort
    vector<int> tmp;
    for (int i = 0; i < res.size(); i++) {
        tmp.push_back(res[i]);
    }
    sort(tmp.begin(), tmp.end());
    vector<int> res1;
    for (int i = 0; i < tmp.size(); i++) {
        res1.push_back(tmp[i]);
    }
    // index
    for (int i = 0; i < res1.size(); i++) {
        for (int j = 0; j < nums.size(); j++) {
            if (res1[i] == res[j]) {
                res.push_back(j);
                break;
            }
        }
    }
    return res;
}

B:
    vector<int> order_by_points(vector<int> nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            while (nums[i]) {
                sum += nums[i] % 10;
                nums[i] /= 10;
            }
            res.push_back(sum);
        }
        vector<int> tmp;
        for (int i = 0; i < res.size(); i++) {
            tmp.push_back(res[i]);
        }
        sort(tmp.begin(), tmp.end());
        vector<int> res1;
        for (int i = 0; i < tmp.size(); i++) {
            res1.push_back(tmp[i]);
        }
        for (int i = 0; i < res1.size(); i