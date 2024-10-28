    int i,j;
    float closest_pair[2];
    float current_min=10000000000000000;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<current_min)
    {
        current_min=abs(numbers[i]-numbers[j]);
        closest_pair[0]=numbers[i];
        closest_pair[1]=numbers[j];
    }
    vector<float> closest_pair_vec;
    closest_pair_vec.push_back(closest_pair[0]);
    closest_pair_vec.push_back(closest_pair[1]);
    return closest_pair_vec;
}




