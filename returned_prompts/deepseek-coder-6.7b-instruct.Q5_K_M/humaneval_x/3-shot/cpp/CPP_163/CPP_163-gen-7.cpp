    vector<int> even_nums;
    int start, end, i;
    if(a>b)
    {
        start=b;
        end=a;
    }
    else
    {
        start=a;
        end=b;
    }
    for(i=start;i<=end;i++)
    {
        if(i%2==0)
        {
            even_nums.push_back(i);
        }
    }
    return even_nums;
}

