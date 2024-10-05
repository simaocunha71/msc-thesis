    int i,j;
    float diff=abs(numbers[0]-numbers[1]);
    vector<float> res;
    res.push_back(numbers[0]);
    res.push_back(numbers[1]);
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<diff)
    {
        diff=abs(numbers[i]-numbers[j]);
        res[0]=numbers[i];
        res[1]=numbers[j];
    }
    return res;
}


