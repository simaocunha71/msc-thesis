    vector<int> ordered_nums;
    int i,n;
    int sum;
    for (i=0;i<nums.size();i++)
    {
        sum=0;
        n=abs(nums[i]);
        while (n!=0)
        {
            sum+=n%10;
            n/=10;
        }
        ordered_nums.push_back(sum);
    }
    sort(ordered_nums.begin(), ordered_nums.end());
    return ordered_nums;
}




