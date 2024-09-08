    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        int num = nums[i];
        if(num > 10){
            int first_digit = num / 10;
            int last_digit = num % 10;
            if(first_digit % 2 != 0 && last_digit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

B:
    int specialFilter(vector<int> nums){
        int count = 0;
        for(int num : nums){
            if(num > 10){
                string str = to_string(num);
                if(str[0] % 2 != 0 && str.back() % 2 != 0){
                    count++;
                }
            }
        }
        return count;
    }
C:
    int specialFilter(vector<int> nums){
        int count = 0;
        for(int num : nums){
            if(num > 10){
                int last = num % 10;
                int first = num / 10 % 10;
                if(first % 2 != 0 && last % 2 != 0){
                    count++;
                }
            }
        }
        return count;
    }
D:
    int specialFilter(vector<int> nums){
        int count = 0;
        for(int num : nums){
            if(num > 10){
                if(to_string(num)[0] % 2 != 0 && to_string(num).back() % 2 != 0){
                    count++;
                }
            }
        }
        return count;
    }
E:
    int specialFilter(vector<int> nums){
        int count = 0;
        for(int num : nums){
            if(num > 10){
                string str = to_string(num);
                for(int i = 0; i < str.size(); i++){
                    if(i == 0 || i == str.size() - 1){
                        if(str[i] % 2 != 0){
                            count++;
                            break;
                        }
                    }
                }
            }
        }
        return count;
    }
F:
    int specialFilter(vector<int> nums){
        int count = 0;
        for(int num : nums){
            if(num > 10){
                int first = num / 10;
                int last = num % 10;
                if(first % 2 != 0 && last % 2 != 0){
                    count++;
                }
            }
        }
       