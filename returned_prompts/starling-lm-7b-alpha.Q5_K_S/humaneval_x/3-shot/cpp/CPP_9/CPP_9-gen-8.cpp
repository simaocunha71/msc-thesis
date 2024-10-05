    vector<int> result;
    int i,j;
    int max;
    for (i=0;i<numbers.size();i++)
    {
        max=numbers[i];
        for (j=i+1;j<numbers.size();j++)
        {
            if (numbers[j]>max) max=numbers[j];
        }
        result.push_back(max);
    }
    return result;
}


