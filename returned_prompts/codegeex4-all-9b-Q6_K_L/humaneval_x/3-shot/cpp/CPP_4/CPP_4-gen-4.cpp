    float mean=0.0;
    float mad=0.0;
    int i;
    int size=numbers.size();
    for (i=0;i<size;i++)
    mean+=numbers[i];
    mean=mean/size;
    for (i=0;i<size;i++)
    mad+=abs(numbers[i]-mean);
    mad=mad/size;
    return mad;
}

