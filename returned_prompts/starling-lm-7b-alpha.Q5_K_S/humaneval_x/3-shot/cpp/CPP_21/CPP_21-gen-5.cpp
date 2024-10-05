    int i;
    float minn=numbers[0];
    float maxn=numbers[0];
    int n=numbers.size();
    for (i=0;i<n;i++)
    {
        if (numbers[i]<minn)
        minn=numbers[i];
        if (numbers[i]>maxn)
        maxn=numbers[i];
    }

    for (i=0;i<n;i++)
    numbers[i]=(numbers[i]-minn)/(maxn-minn);

    return numbers;
}



