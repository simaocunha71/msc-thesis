    vector<int> odd_nums;
    vector<int> all_nums;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        for (j=0;j<x[i];j++)
        {
            if (x[i]%10==(j%2)){
                odd_nums.push_back(x[i]);
                break;
            }
            x[i]/=10;
        }
    }
    sort(odd_nums.begin(),odd_nums.end());
    return odd_nums;
}


