    float min_diff=float(INFINITY);
    float closest_pair[2];
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float diff=fabs(numbers[i]-numbers[j]);
        if (diff<min_diff)
        {
            min_diff=diff;
            closest_pair[0]=numbers[i];
            closest_pair[1]=numbers[j];
        }
    }
    vector<float> result(closest_pair,closest_pair+2);
    return result;
}  



