    int i;
    int sum=0;
    for (i=0;i<numbers.size();i++)
    {
    int j;
    if (numbers[i]==1)
    continue;
    for (j=2;j<numbers[i];j++)
    if (numbers[i]%j==0)
    break;
    if (j==numbers[i])
    sum+=numbers[i];
    }
    return sum;
}

