    float sum=0, mean, abs_diff;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        abs_diff=fabs(numbers[i]-mean);
        sum+=abs_diff;
    }
    mean=sum/numbers.size();

    return mean;
}


