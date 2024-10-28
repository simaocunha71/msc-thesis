    float mean=0;
    int i;
    for (i=0;i<numbers.size();i++)
    mean+=numbers[i];
    mean/=numbers.size();
    
    float mad=0;
    for (i=0;i<numbers.size();i++)
    mad+=abs(numbers[i]-mean);
    mad/=numbers.size();
    return mad;
}


