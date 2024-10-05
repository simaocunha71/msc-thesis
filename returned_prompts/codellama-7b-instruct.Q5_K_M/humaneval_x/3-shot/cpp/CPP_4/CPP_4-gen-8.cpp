    float sum=0.0;
    float mean=0.0;
    int i;
    for (i=0;i<numbers.size();i++)
    sum+=numbers[i];
    mean=sum/numbers.size();

    for (i=0;i<numbers.size();i++)
    sum+=fabs(numbers[i]-mean);
    return sum/numbers.size();
}



