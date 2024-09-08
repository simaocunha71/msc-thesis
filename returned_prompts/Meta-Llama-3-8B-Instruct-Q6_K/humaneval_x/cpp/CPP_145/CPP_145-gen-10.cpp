    vector<pair<int, int>> points;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        points.push_back({sum, i});
    }
    sort(points.begin(), points.end());
    vector<int> result;
    for(int i = 0; i < points.size(); i++){
        result.push_back(nums[points[i].second]);
    }
    return result;
}

B:
    vector<int> order_by_points(vector<int> nums){
        vector<pair<int, int>> points;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            int num = nums[i];
            while(num > 0){
                sum += num % 10;
                num /= 10;
            }
            points.push_back({sum, i});
        }
        sort(points.begin(), points.end());
        vector<int> result;
        for(int i = 0; i < points.size(); i++){
            result.push_back(nums[points[i].second]);
        }
        return result;
    }

C:
    vector<int> order_by_points(vector<int> nums){
        vector<pair<int, int>> points;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            int num = nums[i];
            while(num > 0){
                sum += num % 10;
                num /= 10;
            }
            points.push_back({sum, i});
        }
        sort(points.begin(), points.end());
        vector<int> result;
        for(int i = 0; i < points.size(); i++){
            result.push_back(nums[points[i].second]);
        }
        return result;
    }

D:
    vector<int> order_by_points(vector<int> nums){
        vector<pair<int, int>> points;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            int num = nums[i];
            while(num > 0){
                sum += num % 10;
                num /= 10;
            }
            points.push_back({sum, i});
        }
        sort(points.begin(), points.end());
        vector<int> result;
        for(int i = 0; i < points.size(); i++){
            result.push_back(nums[points[i].second