    int sum=0;
    int product=1;
    for (int i:numbers)
    {
        sum+=i;
        product*=i;
    }
    return {sum, product};
}