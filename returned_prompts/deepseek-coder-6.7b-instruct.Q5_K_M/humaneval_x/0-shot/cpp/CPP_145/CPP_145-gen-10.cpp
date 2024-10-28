    vector<pair<int,int>> points(nums.size());
    for(int i=0; i<nums.size(); i++){
        int sum = 0;
        int num = abs(nums[i]);
        while(num){
            sum += num%10;
            num /= 10;
        }
        points[i] = make_pair(sum, nums[i]);
    }
    sort(points.begin(), points.end());
    for(int i=0; i<points.size(); i++){
        nums[i] = points[i].second;
    }
    return nums;
}
int main()
{
    vector<int> nums={1,11,-1,-11,-12};
    vector<int> res=order_by_points(nums);
    for(int i=0;i<res.size();i++)
    {
        printf("%d ",res[i]);
    }
    return 0;
}
*/
