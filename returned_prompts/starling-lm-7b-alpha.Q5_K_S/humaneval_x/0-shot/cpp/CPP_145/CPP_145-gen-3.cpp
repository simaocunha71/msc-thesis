    vector<int> res;
    int sum,i,n;
    n=nums.size();
    for(i=0;i<n;i++)
    {
        sum=0;
        while(nums[i]!=0)
        {
            sum+=nums[i]%10;
            nums[i]/=10;
        }
        res.push_back(sum);
    }
    sort(res.begin(),res.end());
    vector<int> ans;
    for(i=0;i<n;i++)
    {
        if(res[i]==0)
        continue;
        for(int j=0;j<n;j++)
        {
            if(nums[j]==0)
            continue;
            if(res[i]==sum)
            {
                ans.push_back(nums[j]);
                nums[j]=0;
                break;
            }
        }
    }
    return ans;
}







































































































































































































































































