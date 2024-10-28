    int count = 0;
    for(int i = 0; i < nums.size(); i++) {
        if(nums[i] > 10 && (nums[i] % 10) % 2 != 0 && (nums[i]/10) % 10 % 2 != 0) {
            count++;
        }
    }
    return count;
}