int len = nums.size();

B:
long long min = nums[0];

C:
for(int i = 1; i < len; i++){
D:
long long sum = nums[i];
E:
for(int j = i-1; j >= 0; j--){
F:
sum += nums[j];
G:
if(sum < min)
H:
min = sum;
I:
}
J:
}
K:
return min;
L:
}

M:
int main(){
vector<long long> nums = {2, 3, 4, 1, 2, 4};
printf("%lld", minSubArraySum(nums));
return 0;
}

分析：
A: 定义一个变量 len 来存储 nums 向量的长度。
B: 定义一个变量 min 来存储 nums 向量中的最小子数组和，初始值设为 nums[0]。
C: 使用一个 for 循环遍历 nums 向量的索引从 1 到 len-1。
D: 定义一个变量 sum 来存储当前子数组和，初始值设为 nums[i]。
E: 使用一个嵌套的 for 循环遍历 nums 向量的索引从 i-1 到 0。
F: 将当前索引 j 对应的元素值加到 sum 中。
G: 如果 sum 小于 min，则更新 min 的值为 sum。
H: 返回 min 的值。
