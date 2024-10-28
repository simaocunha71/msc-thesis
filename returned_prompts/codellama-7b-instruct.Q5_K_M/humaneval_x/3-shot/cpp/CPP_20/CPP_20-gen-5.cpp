    int i,j;
    int smallest_diff=INT_MAX;
    float diff;
    int index1=0;
    int index2=0;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        diff=abs(numbers[i]-numbers[j]);
        if (diff<smallest_diff)
        {
            smallest_diff=diff;
            index1=i;
            index2=j;
        }
    }
    return {numbers[index1],numbers[index2]};
}



