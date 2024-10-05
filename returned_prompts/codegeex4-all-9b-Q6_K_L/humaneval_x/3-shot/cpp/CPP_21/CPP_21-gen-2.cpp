    float min=numbers[0];
    float max=numbers[0];
    int i;
    for (i=0;i<numbers.size();i++)
    if (numbers[i]>max)
    max=numbers[i];
    for (i=0;i<numbers.size();i++)
    if (numbers[i]<min)
    min=numbers[i];
    vector<float> rescaled;
    for (i=0;i<numbers.size();i++)
    rescaled.push_back((numbers[i]-min)/(max-min));
    return rescaled;
}

