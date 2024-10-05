    int i;
    float min_val=numbers[0];
    float max_val=numbers[0];
    float range,scale;
    vector<float> rescaled_vec;
    for (i=0;i<numbers.size();i++){
        if (numbers[i]<min_val)
        min_val=numbers[i];
        if (numbers[i]>max_val)
        max_val=numbers[i];
    }
    range=max_val-min_val;
    scale=1.0/range;
    for (i=0;i<numbers.size();i++)
    rescaled_vec.push_back((numbers[i]-min_val)*scale);
    return rescaled_vec;
}


