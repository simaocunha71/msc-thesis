    vector<int> result;
    vector<pair<int, int>> temp;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        temp.push_back({sum, i});
    }
    sort(temp.begin(), temp.end());
    for(int i = 0; i < temp.size(); i++){
        result.push_back(nums[temp[i].second]);
    }
    return result;
}

B:
    vector<int> order_by_points(vector<int> nums){
        if(nums.empty())
            return nums;
        sort(nums.begin(), nums.end(), [&nums](int a, int b){
            int sum_a = 0, sum_b = 0;
            while(a > 0){
                sum_a += a % 10;
                a /= 10;
            }
            while(b > 0){
                sum_b += b % 10;
                b /= 10;
            }
            if(sum_a != sum_b)
                return sum_a < sum_b;
            else
                return find(nums.begin(), nums.end(), a) < find(nums.begin(), nums.end(), b);
        });
        return nums;
    }
C:
    vector<int> order_by_points(vector<int> nums){
        vector<pair<int, int>> temp;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            int num = nums[i];
            while(num > 0){
                sum += num % 10;
                num /= 10;
            }
            temp.push_back({sum, i, nums[i]});
        }
        sort(temp.begin(), temp.end());
        vector<int> result;
        for(int i = 0; i < temp.size(); i++){
            result.push_back(temp[i].back());
        }
        return result;
    }
    // the best solution is B
    // it uses the sort function with a lambda function that calculates the sum of digits for each number
    // and then compares them. If the sums are equal, it compares the original numbers
    // This way, the function is efficient and easy to understand. 
    // It also handles the case where the input vector is empty correctly. 

















// The best solution is B
// It uses the sort function with a lambda function that calculates the sum of digits for each number
//