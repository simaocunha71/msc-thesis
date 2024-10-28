    float sum=0;
    float mean=0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=abs(numbers[i]-mean);
        mean+=numbers[i];
    }
    mean/=numbers.size();
    return sum/numbers.size();
}




