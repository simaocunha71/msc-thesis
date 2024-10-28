    float min_diff=float("inf");
    vector<float> closest_pair;
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float diff=abs(numbers[i]-numbers[j]);
        if (diff<min_diff)
        {
            min_diff=diff;
            closest_pair={numbers[i],numbers[j]};
        }
    }
    return closest_pair;
}
