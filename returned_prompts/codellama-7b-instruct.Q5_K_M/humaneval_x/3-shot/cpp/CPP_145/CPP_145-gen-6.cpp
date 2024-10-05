    int i,j,sum;
    vector<int> ordered_nums;
    vector<int> sums;
    vector<int> indices;
    vector<int> result;
    vector<string> str_nums;
    vector<string> str_sums;
    vector<string> str_indices;
    vector<string> str_result;
    for (i=0;i<nums.size();i++)
    {
    sums.push_back(0);
    indices.push_back(i);
    str_nums.push_back(to_string(nums[i]));
    }
    for (i=0;i<nums.size();i++)
    for (j=i+1;j<nums.size();j++)
    {
        str_sums.push_back(to_string(sums[i]+nums[j]));
        str_indices.push_back(to_string(indices[i]+1));
    }
    for (i=0;i<nums.size();i++)
    for (j=i+1;j<nums.size();j++)
    if (str_sums[i]>str_sums[j])
    {
        sums[i]=sums[j];
        indices[i]=indices[j];
        str_sums[i]=str_sums[j];
        str_indices[i]=str_indices[j];
        sums[j]=sums[i];
        indices[j]=indices[i];
        str_sums[j]=str_sums[i];
        str_indices[j]=str_indices[i];
    }
    for (i=0;i<nums.size();i++)
    {
        result.push_back(nums[i]);
        str_result.push_back(to_string(nums[i]));
    }
    for (i=0;i<nums.size();i++)
    for (j=i+1;j<nums.size();j++)
    if (str_sums[i]