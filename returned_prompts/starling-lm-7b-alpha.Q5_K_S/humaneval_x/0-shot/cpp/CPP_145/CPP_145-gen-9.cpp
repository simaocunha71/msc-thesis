    vector<int> res;
    vector<int> tmp;
    tmp = nums;
    for(int i = 0; i < nums.size(); i++)
    {
        int sum = 0;
        while(tmp[i])
        {
            sum += tmp[i] % 10;
            tmp[i] /= 10;
        }
        res.push_back(sum);
    }
    int min;
    int tmp1;
    for(int i = 0; i < res.size(); i++)
    {
        min = i;
        for(int j = i; j < res.size(); j++)
        {
            if(res[j] < res[min]) min = j;
        }
        tmp1 = res[min];
        res[min] = res[i];
        res[i] = tmp1;
        tmp1 = nums[min];
        nums[min] = nums[i];
        nums[i] = tmp1;
    }
    return nums;
}

B:
    vector<int> res;
    vector<int> tmp;
    tmp = nums;
    for(int i = 0; i < nums.size(); i++)
    {
        int sum = 0;
        while(tmp[i])
        {
            sum += tmp[i] % 10;
            tmp[i] /= 10;
        }
        res.push_back(sum);
    }
    for(int i = 0; i < res.size(); i++)
    {
        int min = i;
        for(int j = i; j < res.size(); j++)
        {
            if(res[j] < res[min]) min = j;
        }
        int tmp1 = res[min];
        res[min] = res[i];
        res[i] = tmp1;
        tmp1 = nums[min];
        nums[min] = nums[i];
        nums[i] = tmp1;
    }
    return nums;
}

