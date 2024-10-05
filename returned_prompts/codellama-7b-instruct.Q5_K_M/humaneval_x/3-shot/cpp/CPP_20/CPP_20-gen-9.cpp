    int i,j;
    float small_diff=10000,diff;
    vector<float> closest_elements;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        diff=abs(numbers[i]-numbers[j]);
        if (diff<small_diff)
        {
            closest_elements.clear();
            closest_elements.push_back(numbers[i]);
            closest_elements.push_back(numbers[j]);
            small_diff=diff;
        }
    }
    return closest_elements;
}


