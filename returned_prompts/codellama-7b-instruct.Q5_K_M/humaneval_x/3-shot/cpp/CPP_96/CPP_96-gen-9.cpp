    vector<int> prime_numbers;
    int i,j;
    for (i=2;i<n;i++)
    {
        for (j=2;j<i;j++)
        if (i%j==0)
        break;
        if (j==i)
        prime_numbers.push_back(i);
    }
    return prime_numbers;
}



