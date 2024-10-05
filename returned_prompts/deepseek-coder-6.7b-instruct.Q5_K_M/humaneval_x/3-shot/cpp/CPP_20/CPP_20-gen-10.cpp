    float min_difference=abs(numbers[0]-numbers[1]);
    int index1=0,index2=1;
    int i,j;
    for(i=0;i<numbers.size();i++)
    for(j=i+1;j<numbers.size();j++)
    {
        if(abs(numbers[i]-numbers[j])<min_difference)
        {
            min_difference=abs(numbers[i]-numbers[j]);
            index1=i;
            index2=j;
        }
    }
    if(index1>index2)
    {
        int temp=index1;
        index1=index2;
        index2=temp;
    }
    return {numbers[index1],numbers[index2]};
}

