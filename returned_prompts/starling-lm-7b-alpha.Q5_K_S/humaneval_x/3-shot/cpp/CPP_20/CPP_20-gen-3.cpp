    int i,j;
    float min_distance=numbers[1]-numbers[0];
    vector<float> closest_elements;
    closest_elements.push_back(numbers[0]);
    closest_elements.push_back(numbers[1]);
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<min_distance)
    {
        min_distance=abs(numbers[i]-numbers[j]);
        closest_elements[0]=numbers[i];
        closest_elements[1]=numbers[j];
    }
    return closest_elements;
}



