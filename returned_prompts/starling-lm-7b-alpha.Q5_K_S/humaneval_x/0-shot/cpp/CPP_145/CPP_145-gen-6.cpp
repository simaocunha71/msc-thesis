    if (nums.size() <= 1) {
        return nums;
    }

    vector<int> left = order_by_points(nums.begin(), nums.begin() + nums.size() / 2);
    vector<int> right = order_by_points(nums.begin() + nums.size() / 2, nums.end());
    vector<int> result;
    int i = 0;
    int j = 0;
    while (i < left.size() && j < right.size()) {
        int leftSum = sum(left[i]);
        int rightSum = sum(right[j]);
        if (leftSum == rightSum) {
            result.push_back(left[i]);
            result.push_back(right[j]);
            i++;
            j++;
        } else if (leftSum < rightSum) {
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }
    return vector_merge(left, result, right);
}

vector<int> vector_merge(vector<int> left, vector<int> middle, vector<int> right) {
    vector<int> result;
    int i = 0;
    int j = 0;
    while (i < left.size() && j < right.size()) {
        int leftSum = sum(left[i]);
        int rightSum = sum(right[j]);
        if (leftSum == rightSum) {
            result.push_back(left[i]);
            result.push_back(right[j]);
            i++;
            j++;
        } else if (leftSum < rightSum) {
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }
    return vector_merge(result, left, right);
}

vector<int> vector_merge(vector<int> left, vector<int> middle, vector<int> right) {
    vector