    int i,j;
    int min_dist=99999;
    float first,second;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<min_dist)
    {
        min_dist=abs(numbers[i]-numbers[j]);
        first=numbers[i];
        second=numbers[j];
    }
    return {first,second};
}

