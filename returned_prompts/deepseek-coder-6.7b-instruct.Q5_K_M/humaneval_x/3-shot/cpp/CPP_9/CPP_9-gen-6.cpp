    int max=numbers[0];
    for  (int i=0;i<numbers.size();i++)
    {
        if  (numbers[i]>max)
        max=numbers[i];
        numbers[i]=max;
    }
    return numbers;
}


