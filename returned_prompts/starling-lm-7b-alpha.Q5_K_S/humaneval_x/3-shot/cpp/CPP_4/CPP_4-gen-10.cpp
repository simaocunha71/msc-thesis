    float mean = 0.0;
    int i;
    for (i=0;i<numbers.size();i++)
    mean+=numbers[i];
    mean/=numbers.size();

    float mad=0.0;
    for (i=0;i<numbers.size();i++)
    mad+=fabs(numbers[i]-mean);
    return mad/numbers.size();
}



