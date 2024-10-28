    int i,j;
    float closest_pair[2];
    float closest_diff=100000000;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float temp_diff=abs(numbers[i]-numbers[j]);
        if (temp_diff<closest_diff)
        {
            closest_diff=temp_diff;
            closest_pair[0]=numbers[i];
            closest_pair[1]=numbers[j];
        }
    }
    vector<float> closest_pairs;
    closest_pairs.push_back(closest_pair[0]);
    closest_pairs.push_back(closest_pair[1]);
    return closest_pairs;
}


