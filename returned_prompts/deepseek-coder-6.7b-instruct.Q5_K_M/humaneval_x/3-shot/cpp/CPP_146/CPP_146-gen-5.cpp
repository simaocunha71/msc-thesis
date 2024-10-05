    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 10) {
            string str = to_string(abs(nums[i]));
            if ((str[0] - '0') % 2 == 1 && (str[str.length() - 1] - '0') % 2 == 1) {
                count++;
            }
        }
    }
    return count;
}

