    vector<int> result = nums;
    vector<int> sums;
    for (int i = 0; i < result.size(); i++) {
        int sum = 0;
        int temp = result[i];
        while (temp != 0) {
            sum += temp % 10;
            temp /= 10;
        }
        sums.push_back(sum);
    }
    sort(sums.begin(), sums.end());
    for (int i = 0; i < sums.size(); i++) {
        int j = 0;
        while (result[j].sum != sums[i]) {
            j++;
        }
        result.erase(result.begin() + j);
        result.insert(result.begin() + i, result[j]);
    }
    return result;
}

B:
    vector<int> order_by_points(vector<int> nums){
        vector<int> result = nums;
        vector<int> sums;
        for (int i = 0; i < result.size(); i++) {
            int sum = 0;
            int temp = result[i];
            while (temp != 0) {
                sum += temp % 10;
                temp /= 10;
            }
            sums.push_back(sum);
        }
        sort(sums.begin(), sums.end());
        for (int i = 0; i < sums.size(); i++) {
            int j = 0;
            while (result[j].sum != sums[i]) {
                j++;
            }
            result.erase(result.begin() + j);
            result.insert(result.begin() + i, result[j]);
        }
        return result;
    }

C:
    vector<int> order_by_points(vector<int> nums){
        vector<int> result = nums;
        vector<int> sums;
        for (int i = 0; i < result.size(); i++) {
            int sum = 0;
           