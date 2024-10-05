    for(auto& x:nums)
        if(x<0)
            x=-x;
    sort(nums.begin(),nums.end(),[](int a,int b)
    {
        int sa=sum_of_digits(a);
        int sb=sum_of_digits(b);
        if(sa==sb)
            return a<b;
        return sa<sb;
    });
    return nums;
}
vector<int> order_by_points(vector<int> nums)
{
    for(auto& x:nums)
        if(x<0)
            x=-x;
    sort(nums.begin(),nums.end(),[](int a,int b)
    {
        int sa=sum_of_digits(a);
        int sb=sum_of_digits(b);
        if(sa==sb)
            return a<b;
        return sa<sb;
    });
    return nums;
}

B:

vector<int> order_by_points(vector<int> nums)
{
    vector<int> order;
    for(auto& x:nums)
        if(x<0)
            x=-x;
    sort(nums.begin(),nums.end(),[](int a,int b)
    {
        int sa=sum_of_digits(a);
        int sb=sum_of_digits(b);
        if(sa==sb)
            return a<b;
        return sa<sb;
    });
    for(int i=0;i<nums.size();i++)
        order.push_back(nums[i]);
    return order;
}

C:

vector<int> order_by_points(vector<int> nums)
{
    vector<int> order;
    for(auto& x:nums)
        if(x<0)
            x=-x;
    sort(nums.begin(),nums.end(),[](int a,int b)
    {
        int sa=sum_of_digits(a);