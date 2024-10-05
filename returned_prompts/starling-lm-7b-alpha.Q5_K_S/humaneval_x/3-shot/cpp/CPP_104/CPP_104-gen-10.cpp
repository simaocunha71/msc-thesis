    vector<int> all_nums;
    vector<int> result;
    int i;
    for (i=0;i<x.size();i++)
    {
        if (x[i]%2==0) continue;
        int curr_num=x[i];
        while (curr_num>0)
        {
            all_nums.push_back(curr_num%10);
            curr_num/=10;
        }
        bool valid=true;
        int j;
        for (j=0;j<result.size();j++)
        if (result[j]==all_nums[j]) valid=false;
        if (valid)
        {
            sort(all_nums.begin(),all_nums.end());
            result.push_back(x[i]);
        }
        all_nums.clear();
    }
    sort(result.begin(),result.end());
    return result;
}



