    float min_diff=float_MAX;
    float closest_pair[2];
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float diff=abs(numbers[i]-numbers[j]);
        if (diff<min_diff)
        {
            min_diff=diff;
            closest_pair[0]=numbers[i];
            closest_pair[1]=numbers[j];
        }
    }
    return vector<float>(closest_pair, closest_pair+2);
}
