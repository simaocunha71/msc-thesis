    float mean=0.0;
    float mad=0.0;
    float dev;
    int i;
    for (i=0;i<numbers.size();i++)
    mean+=numbers[i];
    mean/=numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        dev=numbers[i]-mean;
        mad+=abs(dev);
    }
    mad/=numbers.size();
    return mad;
}


