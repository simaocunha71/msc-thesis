    float min_val=numbers[0];
    float max_val=numbers[0];
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]<min_val)
        min_val=numbers[i];
        if (numbers[i]>max_val)
        max_val=numbers[i];
    }
    vector<float> rescaled_vals;
    for (i=0;i<numbers.size();i++)
    {
        rescaled_vals.push_back((numbers[i]-min_val)/(max_val-min_val));
    }
    return rescaled_vals;
}


