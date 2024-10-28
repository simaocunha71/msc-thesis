    vector<int> result;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        result.push_back(fact(i));
        else
        result.push_back(sum_numbers(i));
    }
    return result;
}
int sum_numbers(int n){
    int result=0;
    int i;
    for (i=1;i<=n;i++)
    result+=i;
    return result;
}
int fact(int n){
    int result=1;
    int i;
    for (i=1;i<=n;i++)
    result*=i;
    return result;
}


