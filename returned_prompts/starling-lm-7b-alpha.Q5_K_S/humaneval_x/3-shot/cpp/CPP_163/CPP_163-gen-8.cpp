    vector<int> all_nums;
    int i,j;
    for (i=a;i<=b;i++)
    {
        j=i;
        while (j>0)
        {
        if (j%2==0){
            all_nums.push_back(j);
        }
        j/=10;
        }
    }
    return all_nums;
}

