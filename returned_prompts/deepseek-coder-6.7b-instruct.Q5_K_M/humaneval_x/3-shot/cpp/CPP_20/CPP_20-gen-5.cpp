    float min_difference=1000000000;
    float difference;
    float min_first,min_second;
    int i,j;
    for  (i=0;i<numbers.size();i++)
    for  (j=i+1;j<numbers.size();j++)
    {
        difference=abs(numbers[i]-numbers[j]);
        if  (difference<min_difference)
        {
            min_difference=difference;
            min_first=numbers[i];
            min_second=numbers[j];
        }
    }
    return {min_first,min_second};
}

