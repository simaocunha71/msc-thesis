    int count = 0;
    for(int i=0; i<nums.size(); i++){
        int num = abs(nums[i]);
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
int main() {
    vector<int> nums = {15, -73, 14, -15};
    printf("%d\n", specialFilter(nums));
    nums = {33, -2, -3, 45, 21, 109};
    printf("%d\n", specialFilter(nums));
    return 0;
}
