    int i,j;
    vector<float> closest;
    float current_diff,min_diff;
    float current_num,min_num;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        current_num=numbers[i];
        current_diff=abs(numbers[j]-numbers[i]);
        if (current_diff<min_diff || (current_diff==min_diff && current_num<min_num))
        {
            min_diff=current_diff;
            min_num=current_num;
        }
    }
    closest.push_back(min_num);
    closest.push_back(numbers[i]);
    return closest;
}


