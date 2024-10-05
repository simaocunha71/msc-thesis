    sort(numbers.begin(), numbers.end());
    float min_difference=numbers[1]-numbers[0];
    int i;
    for  (i=1;i<numbers.size()-1;i++)
    {
        if  (numbers[i+1]-numbers[i]<min_difference)
        min_difference=numbers[i+1]-numbers[i];
    }

    for  (i=1;i<numbers.size()-1;i++)
    {
        if  (numbers[i+1]-numbers[i]==min_difference)
        return {numbers[i], numbers[i+1]};
    }

    return {numbers[0], numbers[1]};
}


