    vector<int> even_numbers;
    int i,j;
    if(a>b)
    {
        i=b;
        j=a;
    }
    else
    {
        i=a;
        j=b;
    }
    for(i;i<=j;i++)
    {
        if(i%2==0)
        even_numbers.push_back(i);
    }
    return even_numbers;
}

