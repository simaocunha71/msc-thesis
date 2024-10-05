    float min_val=*min_element(numbers.begin(),numbers.end());
    float max_val=*max_element(numbers.begin(),numbers.end());
    float range_val=max_val-min_val;
    vector<float> rescaled_numbers;
    for (int i=0;i<numbers.size();i++)
    rescaled_numbers.push_back((numbers[i]-min_val)/range_val);
    return rescaled_numbers;
}



