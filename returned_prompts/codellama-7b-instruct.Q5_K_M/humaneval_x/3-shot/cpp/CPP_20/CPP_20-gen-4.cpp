    int i,j;
    float min_diff=1000000;
    float diff;
    vector<float> closest_nums;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        diff=numbers[i]-numbers[j];
        if (abs(diff)<min_diff)
        {
        min_diff=abs(diff);
        closest_nums[0]=numbers[i];
        closest_nums[1]=numbers[j];
        }
    }
    return closest_nums;
}



