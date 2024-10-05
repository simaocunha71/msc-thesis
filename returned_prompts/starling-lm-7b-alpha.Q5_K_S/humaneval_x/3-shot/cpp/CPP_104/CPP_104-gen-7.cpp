    vector<int> all_nums;
    vector<int> odd_digits;
    int i;
    int digit;
    for (i=0;i<x.size();i++)
    {
        all_nums.push_back(x[i]);
    }
    sort(all_nums.begin(),all_nums.end());
    odd_digits.clear();
    for (i=0;i<all_nums.size();i++)
    {
        digit=all_nums[i];
        bool has_odd_digit=false;
        int j;
        for (j=1;j<(int)pow(10,digit)+1;j++)
        {
            if (digit%j==0 && j%2!=0)
            {
                has_odd_digit=true;
                break;
            }
        }
        if (has_odd_digit==false)
        {
            odd_digits.push_back(all_nums[i]);
        }
    }
    sort(odd_digits.begin(),odd_digits.end());
    return odd_digits;
}


