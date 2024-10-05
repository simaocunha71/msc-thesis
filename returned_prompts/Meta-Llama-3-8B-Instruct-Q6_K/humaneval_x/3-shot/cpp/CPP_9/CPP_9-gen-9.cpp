    vector<int> max_rolling;
    int max_so_far = INT_MIN;
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] > max_so_far) {
            max_so_far = numbers[i];
        }
        max_rolling.push_back(max_so_far);
    }
    return max_rolling;
}