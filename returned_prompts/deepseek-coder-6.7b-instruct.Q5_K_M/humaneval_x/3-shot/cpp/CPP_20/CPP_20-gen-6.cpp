    sort(numbers.begin(),numbers.end());
    float diff=numbers[1]-numbers[0];
    float min_diff=diff;
    int i;
    vector<float> closest_elements;
    closest_elements.push_back(numbers[0]);
    closest_elements.push_back(numbers[1]);
    for(i=2;i<numbers.size();i++)
    {
        diff=numbers[i]-numbers[i-1];
        if(diff<min_diff)
        {
            min_diff=diff;
            closest_elements[0]=numbers[i-1];
            closest_elements[1]=numbers[i];
        }
    }
    return closest_elements;
}

