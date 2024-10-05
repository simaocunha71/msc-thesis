    int i,j;
    float closest;
    float current;
    vector<float> closest_nums;
    closest=abs(numbers[0]-numbers[1]);
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        current=abs(numbers[i]-numbers[j]);
        if (current<closest)
        {
            closest=current;
            closest_nums.push_back(numbers[i]);
            closest_nums.push_back(numbers[j]);
        }
    }
    return closest_nums;
}

