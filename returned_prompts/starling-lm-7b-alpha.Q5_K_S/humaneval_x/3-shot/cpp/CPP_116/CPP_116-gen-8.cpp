    vector<int> result;
    int i,j,tmp;
    for (i=0;i<arr.size();i++)
    {
        tmp=arr[i];
        for (j=i;j>=0;j--)
        if ((tmp&(1<<j))!=0)
        {
            tmp&=~(1<<j);
            tmp|=1<<(j-1);
        }
        result.push_back(tmp);
    }
    sort(result.begin(), result.end());
    return result;
}



