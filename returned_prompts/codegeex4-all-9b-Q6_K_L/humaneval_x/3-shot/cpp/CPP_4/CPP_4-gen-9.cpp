    float sum=0;
    float x_mean=0;
    float MAD=0;

    for (int i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
    }
    x_mean=sum/numbers.size();

    for (int i=0;i<numbers.size();i++)
    {
        MAD+=abs(numbers[i]-x_mean);
    }
    MAD=MAD/numbers.size();

    return MAD;
}

