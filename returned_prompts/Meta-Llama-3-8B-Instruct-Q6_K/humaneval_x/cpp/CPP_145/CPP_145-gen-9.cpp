    vector<int> result;
    if(nums.empty()) return result;
    map<int, int> m;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        if(m.find(sum) == m.end()) m[sum] = i;
        else m[sum] = i;
    }
    for(int sum : m){
        for(int num : nums){
            if(sum == m[sum] && m[sum] < 0){
                result.push_back(num);
                break;
            }
        }
    }
    return result;
}

B:
    vector<int> result;
    if(nums.empty()) return result;
    vector<pair<int, int>> v;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        v.push_back({sum, i});
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++){
        result.push_back(nums[v[i].second]);
    }
    return result;
}

C:
    vector<int> result;
    if(nums.empty()) return result;
    vector<pair<int, pair<int, int>>> v;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        v.push_back({sum, {i, nums[i]}});
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++){
        result.push_back(v[i].second.second);
    }
    return result;
}

D:
    sort(nums.begin(), nums.end(), [](int a, int b) {
        int sum1 = 0, sum2 = 0;
        while(a > 0) {
            sum1 += a % 10;
            a /= 10;
        }
        while(b > 0) {
            sum2 += b % 10;
            b /= 10;
        }
        if(sum1 == sum2) return a < b;
