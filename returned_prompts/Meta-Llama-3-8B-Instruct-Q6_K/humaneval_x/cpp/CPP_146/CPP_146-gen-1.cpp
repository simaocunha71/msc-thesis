    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && (nums[i]%10)%2 != 0 && (nums[i]/10)%10%2 != 0){
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> nums = {15, -73, 14, -15};
    int result = specialFilter(nums);
    printf("The result is: %d\n", result);
    return 0;
}

