    vector<pair<int, int>> nums_with_index;
    for (int i = 0; i < nums.size(); i++) {
        nums_with_index.push_back({get_digit_sum(nums[i]), i});
    }
    sort(nums_with_index.begin(), nums_with_index.end());
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        result.push_back(nums[nums_with_index[i].second]);
    }
    return result;
}

int get_digit_sum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}