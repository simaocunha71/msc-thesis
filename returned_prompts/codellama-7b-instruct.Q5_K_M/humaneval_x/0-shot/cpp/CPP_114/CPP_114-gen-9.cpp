    long long min = 100000000000;
    long long sum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        for(int j = i; j < nums.size(); j++){
            if(sum < min){
                min = sum;
            }
            sum += nums[j];
        }
    }
    return min;
}

int main(int argc, char* argv[]){
    vector<long long> nums;
    long long i;
    if(argc == 2){
        nums.push_back(strtoll(argv[1], NULL, 10));
    }
    else{
        for(i = 0; i < 6; i++){
            nums.push_back(strtoll(argv[i+1], NULL, 10));
        }
    }
    long long result = minSubArraySum(nums);
    printf("result: %lld\n", result);
    return 0;
}
