    sort(nums.begin(), nums.end(), [](int a, int b){
        int sum_a = 0, sum_b = 0;
        int a_copy = abs(a), b_copy = abs(b);
        while (a_copy) {
            sum_a += a_copy % 10;
            a_copy /= 10;
        }
        while (b_copy) {
            sum_b += b_copy % 10;
            b_copy /= 10;
        }
        return sum_a < sum_b || (sum_a == sum_b && a < b);
    });
    return nums;
}


