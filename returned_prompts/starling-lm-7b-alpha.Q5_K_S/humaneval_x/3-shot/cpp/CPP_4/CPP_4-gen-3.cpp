    float mean=0;
    int i;
    for (i=0;i<numbers.size();i++)
    mean+=numbers[i];

    mean/=(float)numbers.size();

    float mad=0;
    for (i=0;i<numbers.size();i++)
    mad+=fabs(numbers[i]-mean);

    return mad/(float)numbers.size();
}



