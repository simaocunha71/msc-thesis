    float min_diff=numeric_limits<float>::max();
    float closest_pair[2];
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float diff=numbers[i]-numbers[j];
        if (abs(diff)<min_diff)
        {
            min_diff=abs(diff);
            closest_pair[0]=numbers[i];
            closest_pair[1]=numbers[j];
        }
    }
    vector<float> result;
    result.push_back(closest_pair[0]);
    result.push_back(closest_pair[1]);
    return result;
}

