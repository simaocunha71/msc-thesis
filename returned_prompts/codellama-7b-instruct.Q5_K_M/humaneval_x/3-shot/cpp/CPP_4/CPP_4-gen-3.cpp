    float mean=0;
    float mad=0;
    float diff;
    float sum=0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
    }
    mean=sum/numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        diff=numbers[i]-mean;
        mad+=abs(diff);
    }
    mad/=numbers.size();
    return mad;
}

