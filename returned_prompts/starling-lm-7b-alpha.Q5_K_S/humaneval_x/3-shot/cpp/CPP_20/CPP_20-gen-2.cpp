    int i,j;
    float closest_distance=9999999;
    vector<float> closest_pair;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<closest_distance)
    {
        closest_distance=abs(numbers[i]-numbers[j]);
        closest_pair.clear();
        closest_pair.push_back(numbers[i]);
        closest_pair.push_back(numbers[j]);
    }
    return closest_pair;
}



