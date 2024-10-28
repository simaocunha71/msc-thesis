    float min_diff=float("inf");
    float closest_numbers[2];
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float diff=abs(numbers[i]-numbers[j]);
        if (diff<min_diff)
        {
            min_diff=diff;
            closest_numbers[0]=numbers[i];
            closest_numbers[1]=numbers[j];
        }
    }
    vector<float> result;
    result.push_back(closest_numbers[0]);
    result.push_back(closest_numbers[1]);
    return result;
}