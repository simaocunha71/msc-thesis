    for(int i = 0; i < nums.size(); i++) {
        int sum = 0;
        int tmp = nums[i];
        while(tmp > 0) {
            sum += tmp % 10;
            tmp = tmp / 10;
        }
        nums[i] = sum;
    }

    for(int i = 0; i < nums.size(); i++) {
        for(int j = 0; j < nums.size(); j++) {
            if(nums[i] < nums[j]) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }
        }
    }
    return nums;
}


B:
    vector<int> order_by_points(vector<int> nums){
    vector<int> tmp = nums;
    for(int i = 0; i < tmp.size(); i++) {
        int sum = 0;
        int tmp = tmp[i];
        while(tmp > 0) {
            sum += tmp % 10;
            tmp = tmp / 10;
        }
        tmp[i] = sum;
    }

    for(int i = 0; i < tmp.size(); i++) {
        for(int j = 0; j < tmp.size(); j++) {
            if(tmp[i] < tmp[j]) {
                int tmp = tmp[i];
                tmp[i] = tmp[j];
                tmp[j] = tmp;
            }
        }
    }
    return tmp;
}


C:
vector<int> order_by_points(vector<int> nums){
    vector<int> tmp = nums;
    for(int i = 0; i < tmp.size(); i++) {
        int sum = 0;
        int tmp = tmp[i];
        while(tmp > 0) {
            sum += tmp % 10;
            tmp = tmp / 10;
       