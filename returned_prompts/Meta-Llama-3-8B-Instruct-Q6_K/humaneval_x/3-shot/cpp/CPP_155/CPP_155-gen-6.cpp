    int count_even=0,count_odd=0;
    int n = abs(num);
    while(n>0)
    {
        int digit = n%10;
        if(digit%2==0)
            count_even++;
        else
            count_odd++;
        n=n/10;
    }
    vector<int> result;
    result.push_back(count_even);
    result.push_back(count_odd);
    return result;
}
