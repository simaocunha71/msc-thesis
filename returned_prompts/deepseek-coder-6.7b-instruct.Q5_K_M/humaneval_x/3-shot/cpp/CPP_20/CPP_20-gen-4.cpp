    float min_diff=abs(numbers[1]-numbers[0]);
    float diff;
    int i,j, min_i=0, min_j=1;
    vector<float> closest_pair(2);
    for(i=0; i<numbers.size(); i++)
    {
        for(j=i+1; j<numbers.size(); j++)
        {
            diff=abs(numbers[i]-numbers[j]);
            if(diff<min_diff)
            {
                min_diff=diff;
                min_i=i;
                min_j=j;
            }
        }
    }
    closest_pair[0]=numbers[min_i]<numbers[min_j] ? numbers[min_i] : numbers[min_j];
    closest_pair[1]=numbers[min_i]>numbers[min_j] ? numbers[min_i] : numbers[min_j];
    return closest_pair;
}


