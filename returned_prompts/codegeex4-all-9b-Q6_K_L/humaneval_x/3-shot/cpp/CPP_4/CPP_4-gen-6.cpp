    float avg=0;
    for(int i=0;i<numbers.size();i++)
    avg+=numbers[i];
    avg/=numbers.size();
    float sum=0;
    for(int i=0;i<numbers.size();i++)
    sum+=abs(numbers[i]-avg);
    sum/=numbers.size();
    return sum;
}

