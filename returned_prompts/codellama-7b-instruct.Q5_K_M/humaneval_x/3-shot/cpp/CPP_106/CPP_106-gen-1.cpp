    vector<int> result;
    int i;
    for (i=1;i<=n;i++)
    if (i%2==0){
        result.push_back(i);
    }
    else{
        int sum=0;
        for (i=1;i<=n;i++)
        sum+=i;
        result.push_back(sum);
    }
    return result;
}


