    float min_diff = INFINITY;
    float min_first, min_second;
    int i,j;
    for(i=0;i<numbers.size();i++)
        for(j=i+1;j<numbers.size();j++)
        {
            float diff = abs(numbers[i]-numbers[j]);
            if(diff<min_diff)
            {
                min_diff=diff;
                min_first=numbers[i];
                min_second=numbers[j];
            }
        }
    if(min_first>min_second)
    swap(min_first, min_second);
    vector<float> result={min_first, min_second};
    return result;
}


