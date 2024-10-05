    int i,j;
    vector<float> closest_numbers;
    float current_closest=numbers[0]-numbers[1];
    closest_numbers.push_back(numbers[0]);
    closest_numbers.push_back(numbers[1]);
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<current_closest)
    {
        closest_numbers.clear();
        closest_numbers.push_back(numbers[i]);
        closest_numbers.push_back(numbers[j]);
        current_closest=abs(numbers[i]-numbers[j]);
    }
    return closest_numbers;
}


