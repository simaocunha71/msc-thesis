    float min_diff=1e9;
    float min_diff_num1=0;
    float min_diff_num2=0;
    int i;
    for (i=0;i<numbers.size();i++)
    for (int j=i+1;j<numbers.size();j++)
    {
        float diff=abs(numbers[i]-numbers[j]);
        if (diff<min_diff)
        {
            min_diff=diff;
            min_diff_num1=numbers[i];
            min_diff_num2=numbers[j];
        }
    }
    vector<float> result;
    result.push_back(min_diff_num1);
    result.push_back(min_diff_num2);
    return result;
}