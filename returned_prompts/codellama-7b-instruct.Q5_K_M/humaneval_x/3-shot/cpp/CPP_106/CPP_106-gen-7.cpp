    vector<int> result;
    int factorial=1;
    int sum=0;
    for (int i=1;i<=n;i++){
        if (i%2==0)
        factorial*=i;
        else
        sum+=i;
        result.push_back(factorial);
    }
    return result;
}


