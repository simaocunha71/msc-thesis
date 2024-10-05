    auto sort_by_points = [](const int &a, const int &b) {
        int a_points = 0, b_points = 0;
        a_points = abs(a%10) + (a/10)%10 + (a/100)%10 + (a/1000)%10 + (a/10000)%10 + (a/100000)%10;
        b_points = abs(b%10) + (b/10)%10 + (b/100)%10 + (b/1000)%10 + (b/10000)%10 + (b/100000)%10;
        return a_points < b_points;
    };
    sort(nums.begin(), nums.end(), sort_by_points);
    return nums;
}


