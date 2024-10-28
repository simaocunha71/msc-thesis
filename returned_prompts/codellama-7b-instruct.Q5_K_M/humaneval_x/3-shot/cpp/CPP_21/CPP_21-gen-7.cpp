    float min=numbers[0], max=numbers[0];
    int i;
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]<min)
        min=numbers[i];
        if (numbers[i]>max)
        max=numbers[i];
    }
    vector<float> res;
    for (i=0;i<numbers.size();i++)
    res.push_back((numbers[i]-min)/(max-min));
    return res;
}


