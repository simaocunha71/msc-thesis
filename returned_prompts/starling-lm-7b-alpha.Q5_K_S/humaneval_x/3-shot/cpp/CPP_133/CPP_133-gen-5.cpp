    int i,j;
    vector<int> int_lst;
    for (i=0;i<lst.size();i++)
    {
        int_lst.push_back(int(ceil(lst[i])));
    }
    int sum=0;
    for (i=0;i<int_lst.size();i++)
    {
        sum+=pow(int_lst[i],2);
    }
    return sum;
}



