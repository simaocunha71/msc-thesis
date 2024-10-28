    vector<int> result;
    int i,j;
    for (i=1;i<=n;i++)
    {
        if (i%2==0){
        result.push_back(i);
        for (j=1;j<i;j++)
        result[result.size()-1]*=j;
        }
        if (i%2!=0){
        result.push_back(0);
        for (j=1;j<=i;j++)
        result[result.size()-1]+=j;
        }
    }
    return result;
}


