    vector<int> result;
    vector<pair<int, int>> vec;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        vec.push_back({sum, i});
    }
    sort(vec.begin(), vec.end());
    for(int i = 0; i < vec.size(); i++){
        result.push_back(nums[vec[i].second]);
    }
    return result;
}

B:
    vector<int> order_by_points(vector<int> nums) {
        vector<pair<int, int>> vec;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            int num = nums[i];
            while(num > 0){
                sum += num % 10;
                num /= 10;
            }
            vec.push_back({sum, i});
        }
        sort(vec.begin(), vec.end());
        return vector<int>(vec.begin(), vec.end(), nums);
    }

C:
    vector<int> order_by_points(vector<int> nums) {
        sort(nums.begin(), nums.end(), [](int a, int b) {
            int sumA = 0, sumB = 0;
            while(a > 0) {
                sumA += a % 10;
                a /= 10;
            }
            while(b > 0) {
                sumB += b % 10;
                b /= 10;
            }
            if(sumA == sumB) return a < b;
            return sumA < sumB;
        });
        return nums;
    }

D:
    vector<int> order_by_points(vector<int> nums) {
        sort(nums.begin(), nums.end(), [](int a, int b) {
            int sumA = 0, sumB = 0;
            while(a > 0) {
                sumA += a % 10;
                a /= 10;
            }
            while(b > 0) {
                sumB += b % 10;
                b /= 10;
            }
            if(sumA == sumB) return make_pair(a, nums.size() - 1) < make_pair(b, nums.size() - 1);
            return make_pair(sumA, a) < make_pair(sumB, b);
        });
        return nums;
    }

E:
    vector<int> order