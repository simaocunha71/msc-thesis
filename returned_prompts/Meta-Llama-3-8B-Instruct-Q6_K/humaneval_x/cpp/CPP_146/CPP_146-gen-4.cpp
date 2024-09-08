    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 10 && (nums[i] % 10) % 2 != 0 && (nums[i] / 10) % 10 % 2 != 0) {
            count++;
        }
    }
    return count;
}

B:
    int specialFilter(vector<int> nums) {
        int count = 0;
        for (auto num : nums) {
            if (num > 10) {
                int first_digit = num / 10;
                int last_digit = num % 10;
                if (first_digit % 2 != 0 && last_digit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }

C:
    int specialFilter(vector<int> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                string str = to_string(num);
                if (str[0] % 2 != 0 && str.back() % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }

D:
    int specialFilter(vector<int> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int first_digit = num / 10;
                int last_digit = num % 10;
                if (first_digit % 2 != 0 && last_digit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
E:
    int specialFilter(vector<int> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int last_digit = num % 10;
                int first_digit = num / 10;
                if (last_digit % 2 != 0 && first_digit % 10 % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }

F:
    int specialFilter(vector<int> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int last_digit = num % 10;
                int first_digit = num / 10;
                if (last_digit