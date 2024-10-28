    float mean=0;
    float mad=0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        mad+=abs(numbers[i]-mean);
    }
    mean=mean/numbers.size();
    return mad/numbers.size();
}

