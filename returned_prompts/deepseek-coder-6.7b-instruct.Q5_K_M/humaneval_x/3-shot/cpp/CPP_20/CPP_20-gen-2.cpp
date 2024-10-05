    float min_diff=numbers[1]-numbers[0];
    float diff;
    int i,j;
    float min_first,min_second;
    min_first=numbers[0];
    min_second=numbers[1];
    for(i=0;i<numbers.size();i++)
    for(j=i+1;j<numbers.size();j++)
    {
        diff=abs(numbers[i]-numbers[j]);
        if(diff<min_diff)
        {
            min_diff=diff;
            if(numbers[i]<numbers[j])
            {
                min_first=numbers[i];
                min_second=numbers[j];
            }
            else
            {
                min_first=numbers[j];
                min_second=numbers[i];
            }
        }
    }
    vector<float> result{min_first,min_second};
    return result;
}


