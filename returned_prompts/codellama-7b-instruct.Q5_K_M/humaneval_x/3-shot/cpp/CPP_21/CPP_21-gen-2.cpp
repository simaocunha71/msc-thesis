    float min_val=numbers[0];
    float max_val=numbers[0];
    int i;
    for (i=0;i<numbers.size();i++){
        if (numbers[i]<min_val)
        min_val=numbers[i];
        if (numbers[i]>max_val)
        max_val=numbers[i];
    }
    float range=max_val-min_val;
    vector<float> rescaled_nums;
    for (i=0;i<numbers.size();i++){
        rescaled_nums.push_back((numbers[i]-min_val)/range);
    }
    return rescaled_nums;
}

