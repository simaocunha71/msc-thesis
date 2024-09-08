    int count = 0;
    for(int num : nums){
        if(num > 10 && num > 0){
            string str = to_string(num);
            if(str[0] % 2 != 0 && str[str.length()-1] % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

int main()
{
    vector<int> nums = {15, -73, 14, -15};
    printf("%d\n", specialFilter(nums));
    nums = {33, -2, -3, 45, 21, 109};
    printf("%d\n", specialFilter(nums));
    return 0;
}
