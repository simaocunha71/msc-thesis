    int i;
    float mean=0;
    float sum=0;
    float diff;

    for (i=0;i<numbers.size();i++)
    sum+=numbers[i];
    mean=sum/numbers.size();

    for (i=0;i<numbers.size();i++)
    {
        diff=numbers[i]-mean;
        if (diff<0)
        diff=-diff;
        sum+=diff;
    }

    return sum/numbers.size();
}


