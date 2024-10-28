    int i;
    float max=numbers[0];
    float min=numbers[0];
    float range=numbers[0];
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]>max) max=numbers[i];
        if (numbers[i]<min) min=numbers[i];
        range=max-min;
    }
    vector<float> res;
    for (i=0;i<numbers.size();i++)
    res.push_back((numbers[i]-min)/range);
    return res;
}



