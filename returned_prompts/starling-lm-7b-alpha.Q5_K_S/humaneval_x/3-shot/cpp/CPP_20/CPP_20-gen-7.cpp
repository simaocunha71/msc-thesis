    int i,j;
    float d=100000000;
    vector<float> closest_numbers;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float curr_d=abs(numbers[i]-numbers[j]);
        if (curr_d<d)
        {
            d=curr_d;
            closest_numbers[0]=numbers[i];
            closest_numbers[1]=numbers[j];
        }
    }

    return closest_numbers;
}



