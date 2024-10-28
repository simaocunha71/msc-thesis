    return 0;
}

// 核心思路：
// 1. 找到最小的子数组，如果最小子数组包含的元素为空，则返回整个数组的和
// 2. 如果最小子数组不为空，则找到这个最小子数组的最小值
int main(){
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    long long res = minSubArraySum(nums);
    printf("%lld", res);
    return 0;
}

