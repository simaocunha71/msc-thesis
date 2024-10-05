    int n=abs(num);
    int even_count=0;
    int odd_count=0;
    int digit;
    while (n>0)
    {
        digit=n%10;
        if (digit%2==0)
            even_count+=1;
        else
            odd_count+=1;
        n=int(n/10);
    }
    vector<int> result={even_count, odd_count};
    return result;
}


