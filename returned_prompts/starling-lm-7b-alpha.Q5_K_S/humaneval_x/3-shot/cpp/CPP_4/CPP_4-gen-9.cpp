    float mean=0;
    int i,n=numbers.size();
    for (i=0;i<n;i++)
    mean+=numbers[i];

    mean/=n;
    float mad=0;
    for (i=0;i<n;i++)
    mad+=fabs(numbers[i]-mean);

    return mad/n;
}



