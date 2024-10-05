    float sum_dev=0;
    float mean=0;
    int i;
    for (i=0;i<numbers.size();i++)
    sum_dev+=fabs(numbers[i]-mean);
    mean=numbers[0];
    for (i=1;i<numbers.size();i++)
    mean=(mean+numbers[i])/2.0;
    return sum_dev/numbers.size();
}



