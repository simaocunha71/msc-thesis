return nums;
}
int main()
{
vector<int> nums;
nums.push_back(1);
nums.push_back(11);
nums.push_back(-1);
nums.push_back(-11);
nums.push_back(-12);
vector<int> ans;
ans = order_by_points(nums);
for(int i=0;i<ans.size();i++)
{
printf("%d ", ans[i]);
}
}
