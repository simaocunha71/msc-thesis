    vector<int> res;
    for(int i = 0; i < nums.size(); i++){
        int tmp = abs(nums[i]);
        int sum = 0;
        while(tmp){
            sum += tmp % 10;
            tmp /= 10;
        }
        res.push_back(nums[i]);
    }
    sort(res.begin(), res.end(), [](int a, int b){
        if(abs(a) != abs(b)){
            return abs(a) < abs(b);
        }
        return a < b;
    });
    return res;


}

B:
    vector<int> res;
    for(int i = 0; i < nums.size(); i++){
        int tmp = abs(nums[i]);
        int sum = 0;
        while(tmp){
            sum += tmp % 10;
            tmp /= 10;
        }
        res.push_back(nums[i]);
    }
    sort(res.begin(), res.end(), [](int a, int b){
        if(abs(a) != abs(b)){
            return abs(a) > abs(b);
        }
        return a > b;
    });
    return res;




































































































































































































